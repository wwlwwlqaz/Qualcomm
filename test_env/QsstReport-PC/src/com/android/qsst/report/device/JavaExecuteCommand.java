package com.android.qsst.report.device;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.concurrent.Semaphore;
import java.util.concurrent.TimeUnit;

/**
 * Implementation of the DOS command, and get the implementation of the results
 * of the command
 *
 *
 */
public final class JavaExecuteCommand {

    private StringBuffer mNormalBuffer = null;
    private StringBuffer mErrorBuffer = null;
    private Process process;
    private Semaphore semp = new Semaphore(0);
    private ReadErrorOutput sErrorReadThread = null;

    private static JavaExecuteCommand instance = null;

    private JavaExecuteCommand() {
        super();
    }

    public static JavaExecuteCommand getInstance() {
        if (instance == null) {
            instance = new JavaExecuteCommand();
        }

        return instance;
    }

    public synchronized String[] executeCommand(String command) {
        if (sErrorReadThread == null) {
            sErrorReadThread = new ReadErrorOutput();
            sErrorReadThread.start();
        }
        mNormalBuffer = new StringBuffer();
        mErrorBuffer = new StringBuffer();
        try {
            process = Runtime.getRuntime().exec(command);
            sErrorReadThread.startRead();

            BufferedReader reader = new BufferedReader(new InputStreamReader(
                    process.getInputStream()));
            String out = null;
            while ((out = reader.readLine()) != null) {
                if (out.contains("daemon started successfully")) {
                    // DebugMessage.Print("destroy");
                    process.destroy();
                    sErrorReadThread.stopRead();
                    return new String[] { "", "" };
                } else {
                    mNormalBuffer.append(out + "\n");
                }
            }
            reader.close();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            process = null;
            if (sErrorReadThread != null)
                sErrorReadThread.stopRead();
        }

        return new String[] { String.valueOf(mErrorBuffer).trim(),
                String.valueOf(mNormalBuffer).trim() };
    }

    class ReadErrorOutput extends Thread {
        private BufferedReader reader;
        private InputStreamReader inStreamReader;
        private InputStream inStream;
        private boolean isRun = false;

        public void run() {
            this.setName("error read thread");
            while (true) {
                try {
                    semp.tryAcquire(100, TimeUnit.MILLISECONDS);

                    if (process == null) {
                        continue;
                    }
                    isRun = true;

                    inStream = process.getErrorStream();
                    inStreamReader = new InputStreamReader(inStream);
                    reader = new BufferedReader(inStreamReader);
                    String out = null;
                    try {
                        while ((out = reader.readLine()) != null) {
                            if (out.contains("daemon started successfully")) {
                                // DebugMessage.Print("destroy");
                                process.destroy();
                                break;
                            } else {
                                mErrorBuffer.append(out + "\n");
                            }
                        }
                        reader.close();
                    } catch (Exception e) {
                        // e.printStackTrace();
                    }
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                isRun = false;
            }

        }

        public void startRead() {
            semp.release();
        }

        public void stopRead() {
            if (isRun) {
                int waitTime = 2000;
                while (isRun) {
                    try {
                        Thread.sleep(100);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }

                    waitTime -= 100;

                    if (waitTime < 0) {
                        // DebugMessage.Print("Error output stream read ...........................");
                        sErrorReadThread = null;
                        // this.interrupt();
                        break;
                    }
                }
            }
        }

        public boolean isRun() {
            return isRun;
        }
    }

    public static String getOperationSystemCMD() {
        String OSName = System.getProperty("os.name");
        if (OSName.equals("windows 95") || OSName.equals("windows 98")) {
            return "command.exe /c ";
        } else {
            return "cmd.exe /c ";
        }
    }
}