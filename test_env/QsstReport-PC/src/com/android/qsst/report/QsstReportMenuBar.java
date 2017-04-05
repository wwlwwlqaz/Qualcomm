package com.android.qsst.report;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;

public class QsstReportMenuBar extends JMenuBar implements ActionListener {

    /**
     *
     */
    private static final long serialVersionUID = 1L;

    private QsstReport mQsstReport = null;

    private JMenu mFileMenu = null;
    private JMenu mSettingsMenu = null;
    private JMenu mHelpMenu = null;

    private JMenuItem mExit = null;
    private JMenuItem mAbout = null;
    private JMenuItem mHelp = null;
    private JMenuItem mPreference = null;

    public QsstReportMenuBar(QsstReport instance) {
        mQsstReport = instance;

        mFileMenu = new JMenu("File");
        mFileMenu.setMnemonic('F');

        mExit = new JMenuItem("Exit     Alt+F4");
        mExit.setMnemonic('E');
        mExit.addActionListener(this);
        mFileMenu.add(mExit);

        mSettingsMenu = new JMenu("Settings");
        mSettingsMenu.setMnemonic('S');

        mPreference = new JMenuItem("Config Logging Workspace");
        mPreference.setMnemonic('C');
        mPreference.addActionListener(this);
        mSettingsMenu.add(mPreference);

        mHelpMenu = new JMenu("Help");
        mHelpMenu.setMnemonic('H');

        // mHelp = new JMenuItem("Help");
        // mHelp.setMnemonic('H');
        // mHelp.addActionListener(this);
        // mHelpMenu.add(mHelp);

        mAbout = new JMenuItem("About Qsst Report");
        mAbout.setMnemonic('A');
        mAbout.addActionListener(this);
        mHelpMenu.add(mAbout);

        this.add(mFileMenu);
        this.add(mSettingsMenu);
        this.add(mHelpMenu);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        Object event = e.getSource();
        if (event == mExit) {
            System.exit(0);
        } else if (event == mAbout) {
            (new AboutDialog(mQsstReport)).setVisible(true);
        } else if (event == mHelp) {
            showHelp();
        } else if (event == mPreference) {
            (new InitDialog(mQsstReport)).setVisible(true);
        }
    }

    public void showHelp() {
        System.out.println("Show Help");
    }

}
