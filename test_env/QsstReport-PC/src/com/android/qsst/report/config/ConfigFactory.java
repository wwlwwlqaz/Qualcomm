package com.android.qsst.report.config;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

import com.android.qsst.report.Constant;

public class ConfigFactory {

    private static ConfigFactory mInstance = null;
    private Workspace mWorkspace =null;
    private ConfigFactory() {
    }

    public static ConfigFactory getInstance() {
        if(mInstance ==null) {
            mInstance = new ConfigFactory();
        }
        return mInstance;
    }

    public boolean saveLoggingWorkspace(Workspace workspace) {
        File file =new File(Constant.CONFIG_PATH);
        if(!file.exists()) {
            try {
                file.createNewFile();
            } catch (IOException e) {
                e.printStackTrace();
                return false;
            }
        }

        FileOutputStream fos =null;
        BufferedWriter writer = null;
        try {
            fos = new FileOutputStream(file);
            writer = new BufferedWriter( new OutputStreamWriter(fos));
            writer.write(Workspace.LOGGING+Workspace.DIVIDE+workspace.getLoggingDir());
            writer.flush();
            mWorkspace = workspace;
            return true;
        }catch(Exception e) {
            e.printStackTrace();
            return false;
        }finally {
            if(fos !=null) {
                try{
                    fos.close();
                }catch(Exception e) {
                    e.printStackTrace();
                }
            }
            if(writer !=null) {
                try{
                    writer.close();
                }catch(Exception e) {
                    e.printStackTrace();
                }
            }
        }
    }

    public Workspace getLoggingWorkspace() {
        File file =new File(Constant.CONFIG_PATH);
        if(!file.exists()) {
            mWorkspace =null;
        } else{
            if(mWorkspace == null) {
                FileInputStream fis =null;
                BufferedReader reader = null;
                try {
                    fis = new FileInputStream(file);
                    reader = new BufferedReader(new InputStreamReader(fis));
                    String line = null;
                    while ( (line = reader.readLine())!=null) {
                        int index = line.indexOf(Workspace.DIVIDE);
                        if(index>0 && index !=(line.length() - 1)) {
                            mWorkspace = new Workspace();
                            String prefix = line.substring(0, index);
                            String remain = line.substring(index+1, line.length());
                            if(Workspace.LOGGING.equals(prefix)) {
                                mWorkspace.setLoggingDir(remain);
                            } else {
                                mWorkspace = null;
                            }
                        }
                    }
                }catch(Exception e) {
                    e.printStackTrace();
                    mWorkspace = null;
                }finally {
                    if(fis !=null) {
                        try{
                            fis.close();
                        }catch(Exception e) {
                            e.printStackTrace();
                        }
                    }
                    if(reader !=null) {
                        try{
                            reader.close();
                        }catch(Exception e) {
                            e.printStackTrace();
                        }
                    }
                }
            }
        }
        return mWorkspace;
    }
}
