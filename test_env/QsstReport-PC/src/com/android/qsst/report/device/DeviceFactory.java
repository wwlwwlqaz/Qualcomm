package com.android.qsst.report.device;

import java.util.ArrayList;

import com.android.qsst.report.check.bean.DeviceBean;
import com.android.qsst.report.util.ReportUtils;

/**
 * Received the results of command execution, and get the connection
 * device-related properties
 *
 *
 */
public class DeviceFactory {

    // private static int mStartPort = 10929;

    /**
     * Get list of connected devices, including equipment serial numbers and
     * connection status
     *
     * @return <br />
     *         The list of connected devices
     */
    public static ArrayList<DeviceBean> getDevices() {
        JavaExecuteCommand executeCMD = JavaExecuteCommand.getInstance();
        ArrayList<DeviceBean> devices = new ArrayList<DeviceBean>();

        // Get normal connected devices
        String executeResult = executeCMD.executeCommand(Commands.ADB_DEVICES)[1];
        String filterString = "List of devices attached";
        if (executeResult.contains(filterString)
                && !executeResult.equals(filterString)) {
            // Get list of connected devices
            executeResult = executeResult.substring(executeResult
                    .lastIndexOf(filterString) + filterString.length());
            String[] lines = executeResult.split("\n");
            for(String line :lines) {
                if(!ReportUtils.isEmpty(line)) {
                    DeviceBean device = new DeviceBean();
                    String[] infos = line.split("\t");
                    if(infos.length >=2) {
                        device.setSn(infos[0]);
                        device.setStatus(infos[1]);
                        devices.add(device);
                    }
                }
            }
        }
        return devices;
    }
}
