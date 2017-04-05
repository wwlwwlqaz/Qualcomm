package com.android.qsst.report;

import java.awt.Color;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JEditorPane;
import javax.swing.JLabel;
import javax.swing.JPanel;

import com.android.qsst.report.util.QsstResourse;

public class AboutDialog extends JDialog implements ActionListener {

    /**
       *
       */
    private static final long serialVersionUID = 1L;

    private static final String STR_COPYRIGHT = "Copyright (C) Qualcomm. All rights reserved.";

    private QsstReport mQsstReport = null;

    private JPanel mAboutPanel = null;

    private JLabel mDisLabel = null;
    private JButton mOKBtn = null;

    public AboutDialog(QsstReport instance) {
        super(instance, true);

        mQsstReport = instance;

        this.setTitle(Constant.APP_NAME + " - " + Constant.APP_VERSION);
        this.setBounds(mQsstReport.getX() + mQsstReport.getWidth() / 2 - 250,
                mQsstReport.getY() + mQsstReport.getHeight() / 2 - 125, 500,
                250);
        this.setIconImage(QsstResourse.app_icon.getImage());

        mAboutPanel = new JPanel(null);
        mAboutPanel.setBounds(0, 0, 500, 250);
        mAboutPanel.setOpaque(false);

        mDisLabel = new JLabel(Constant.APP_NAME);
        mDisLabel.setFont(new Font(this.getFont().getName(), Font.BOLD, 30));
        mDisLabel.setForeground(Color.BLACK);
        mDisLabel.setBounds(150, 20, 500, 50);

        JPanel details = new JPanel(new GridLayout(3, 1));
        details.setBounds(20, 80, 500, 80);
        details.setOpaque(false);

        JLabel version = new JLabel("Version: " + Constant.APP_VERSION);

        JLabel copyright = new JLabel(STR_COPYRIGHT);

        JEditorPane mailPane = new JEditorPane();
        mailPane.setContentType("text/html");
        mailPane.setEditable(false);
        mailPane.setOpaque(false);
        mailPane.setText("<html><body><a href='http://www.qualcomm.com/'>"
                + "<font color=#000000 size=3>http://www.qualcomm.com/</font></a>"
                + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                + "<a href=mailto:c_lqiang@qti.qualcomm.com>"
                + "<font color=#000000 size=3>c_lqiang@qti.qualcomm.com"
                + "</font></a></body></html>");
        details.add(version);
        details.add(copyright);
        details.add(mailPane);

        mOKBtn = new JButton("OK");
        mOKBtn.addActionListener(this);
        mOKBtn.setBounds(380, 180, 80, 25);

        mAboutPanel.add(mDisLabel);
        mAboutPanel.add(details);
        mAboutPanel.add(mOKBtn);

        this.add(mAboutPanel);
        setResizable(false);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        Object event = e.getSource();
        if (event == mOKBtn) {
            this.setVisible(false);
            this.dispose();
        }
    }

}
