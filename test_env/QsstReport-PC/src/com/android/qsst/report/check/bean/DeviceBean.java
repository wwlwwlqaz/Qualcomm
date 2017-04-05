package com.android.qsst.report.check.bean;



public class DeviceBean extends CheckBean {

    private String sn;
    private String status;
    public String getSn() {
        return sn;
    }
    public void setSn(String sn) {
        this.sn = sn;
    }
    public String getStatus() {
        return status;
    }
    public void setStatus(String status) {
        this.status = status;
    }
}
