package com.android.qsst.report.util;

import java.net.URL;

import javax.swing.ImageIcon;

public class QsstResourse {
    private static ClassLoader loder = ClassLoader.getSystemClassLoader();

    public static URL url_icon = loder.getResource("images/icon.png");

    public static ImageIcon app_icon = new ImageIcon(url_icon);

    private QsstResourse instance = null;

    private QsstResourse() {
        instance = this;
    }

    public QsstResourse getInstance() {
        if (instance == null) {
            instance = new QsstResourse();
        }
        return instance;
    }
}
