package com.android.qsst.report.device;

public final class Commands {
    /**
     * OS platform DOS command
     */
    public final static String OS_DOS_COMMAND = JavaExecuteCommand
            .getOperationSystemCMD();
    /**
     * adb devices
     */
    public final static String ADB_DEVICES = OS_DOS_COMMAND + "adb devices";
    /**
     * adb pull
     */
    public final static String ADB_SHELL_PULL = OS_DOS_COMMAND
            + "adb -s [SN]  pull \"[arg1]\"  \"[arg2]\"";

    public final static String ADB_SHELL_LOGGING_PATH = OS_DOS_COMMAND
            + "adb -s [SN]  shell python /data/test_env/logging_path.py";
}
