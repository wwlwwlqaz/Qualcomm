package com.android.qsst.report.util;

import java.text.SimpleDateFormat;
import java.util.Date;

import javax.swing.UIManager;

public class ReportUtils {
    private   static final String DATE_FORMATE= "yyyy-MM-dd HH:mm:ss";

    public static void setLookAndFeel() {
        try {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
            // UIManager.setLookAndFeel("com.sun.java.swing.plaf.motif.MotifLookAndFeel");
        } catch (Exception exc) {
            exc.printStackTrace();
        }
    }

    public static String getTime() {
        return (new SimpleDateFormat(DATE_FORMATE)).format(new Date(System
                .currentTimeMillis()));
    }

    public static boolean isEmpty(String text) {
        if(text == null || "".equals(text)) {
            return true;
        }
        return false;
    }
}
