package com.android.qsst.report.check.bean;

public abstract class CheckBean {
    private boolean check = false;

    public boolean isCheck() {
        return check;
    }

    public void setCheck(boolean check) {
        this.check = check;
    }

}
