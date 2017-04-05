package com.android.qsst.report;

import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.util.Timer;
import java.util.TimerTask;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JFileChooser;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.filechooser.FileFilter;

import com.android.qsst.report.config.ConfigFactory;
import com.android.qsst.report.config.Workspace;
import com.android.qsst.report.util.QsstResourse;
import com.android.qsst.report.util.ReportUtils;

/**
 *
 * @author kris
 * @since May 6, 2013
 * @version 1.0.0
 */
public class InitDialog extends JDialog implements ActionListener {

    private static final long serialVersionUID = 1L;
    private static final String BUTTON_CMD_BROWSE = "bro";
    private static final int DIALOG_WIDTH = 400;
    private static final int DIALOG_HEIGHT = 170;

    private QsstReport mQsstReport = null;
    private INotification mNotification = null;
    private File mSelectDir = null;

    private JPanel mAboutPanel = null;

    private JLabel mDisLabel = null;
    private JLabel mErrorLabel = null;
    private JTextField mLoggingDir = null;
    private JButton mBrowse = null;
    private JButton mOKBtn = null;
    private Timer mTimer = null;

    public InitDialog(QsstReport instance) {
        this(instance, null);
    }
    public InitDialog(QsstReport instance, INotification notification) {
        this(instance, notification, null);
    }

    public InitDialog(QsstReport instance, INotification notification,String message) {

        super(instance, true);

        mQsstReport = instance;
        mNotification = notification;

        this.setTitle("Init your report workspace");
        this.setBounds(mQsstReport.getX() + mQsstReport.getWidth() / 2 - DIALOG_WIDTH / 2, mQsstReport.getY() + mQsstReport.getHeight() / 2 - DIALOG_HEIGHT / 2, DIALOG_WIDTH, DIALOG_HEIGHT);
        this.setIconImage(QsstResourse.app_icon.getImage());

        mAboutPanel = new JPanel(null);
        mAboutPanel.setBounds(0, 0, DIALOG_WIDTH, DIALOG_HEIGHT);
        mAboutPanel.setOpaque(false);

        mDisLabel = new JLabel( "select a directory to be your default logging workspace:");
        mDisLabel.setForeground(Color.BLACK);
        mDisLabel.setBounds(20, 20, DIALOG_WIDTH, 25);

        mLoggingDir = new JTextField();
        mLoggingDir.setBounds(20, 50, 250, 25);
        mLoggingDir.setEditable(false);
        Workspace workspace = ConfigFactory.getInstance().getLoggingWorkspace();
        if(workspace!=null) {
            String loggingPath = workspace.getLoggingDir();
            mSelectDir = new File(loggingPath);
            mLoggingDir.setText(loggingPath);
        }

        mBrowse = new JButton("Browse");
        mBrowse.setBounds(290, 50, 80, 25);
        mBrowse.setActionCommand(BUTTON_CMD_BROWSE);
        mBrowse.setToolTipText("Select the dir");
        mBrowse.addActionListener(this);

        mErrorLabel = new JLabel();
        mErrorLabel.setForeground(Color.RED);
        mErrorLabel.setVisible(false);
        mErrorLabel.setBounds(20, 80, DIALOG_WIDTH, 25);

        mOKBtn = new JButton("OK");
        mOKBtn.addActionListener(this);
        mOKBtn.setBounds((DIALOG_WIDTH-80)/2, 100, 80, 25);

        mAboutPanel.add(mDisLabel);
        mAboutPanel.add(mLoggingDir);
        mAboutPanel.add(mBrowse);
        mAboutPanel.add(mErrorLabel);
        mAboutPanel.add(mOKBtn);

        this.add(mAboutPanel);
        setResizable(false);
        if(!ReportUtils.isEmpty(message)) {
            showErrorMessage(message);
        }
    }
    public void showErrorMessage(String error) {
        mErrorLabel.setText(error);
        mErrorLabel.setVisible(true);
        mQsstReport.addLogging(error);

        if(mTimer!=null) {
            mTimer.cancel();
            mTimer = null;
        }
        mTimer = new Timer("Display");
        mTimer.schedule(new TimerTask() {
            @Override
            public void run() {
                mErrorLabel.setText("");
                mErrorLabel.setVisible(false);
            }
        }, 5000);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        Object event = e.getSource();
        if (event == mOKBtn) {
            if(mSelectDir==null) {
                showErrorMessage("Select a directory firstly.");
            } else if(!mSelectDir.exists()){
                showErrorMessage("This directory is not unavailable.");
            } else{
                Workspace workspace = new Workspace();
                workspace.setLoggingDir(mSelectDir.getAbsolutePath());
                if(ConfigFactory.getInstance().saveLoggingWorkspace(workspace)){
                    if(mNotification!=null ) {
                        mNotification.refresh(mSelectDir);
                    }
                    mQsstReport.addLogging("Set the default logging directory:"+mSelectDir.getAbsolutePath());
                    this.setVisible(false);
                    this.dispose();
                } else {
                    showErrorMessage("Init the workspcae failed, please try again.");
                }
            }
        } else if (event == mBrowse) {
            mErrorLabel.setVisible(false);
            browseFile();
        }
    }

    private void browseFile() {
        JFileChooser fileChooser = new JFileChooser();
        fileChooser.setCurrentDirectory(mSelectDir == null ? new File("."):mSelectDir);
        fileChooser.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);
        fileChooser.setFileFilter(new FileFilter() {
            public boolean accept(File file) {
                if (file.isDirectory()) {
                    return true;
                }
                return false;
            }

            @Override
            public String getDescription() {
                return "Your logging directory";
            }

        });
        if (fileChooser.showOpenDialog(this) == JFileChooser.APPROVE_OPTION) {
            mSelectDir = fileChooser.getSelectedFile();
            mLoggingDir.setText(mSelectDir.getAbsolutePath());
        }
    }
}
