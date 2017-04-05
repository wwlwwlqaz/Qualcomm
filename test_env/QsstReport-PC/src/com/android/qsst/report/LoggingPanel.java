package com.android.qsst.report;

import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.HeadlessException;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.filechooser.FileNameExtensionFilter;
import javax.swing.text.BadLocationException;

import com.android.qsst.report.util.ReportUtils;

public class LoggingPanel extends JPanel implements ActionListener {

    /**
     *
     */
    private static final long serialVersionUID = 1L;

    private static final String FILTER_FORMATE = ".qsst";

    private static final String BUTTON_CMD_SAVE = "SAVE";
    private static final String BUTTON_CMD_CLEAR = "CLEAR";

    private JButton mSavebtn = null;
    private JButton mClearbtn = null;
    private JTextArea mCmdDetaiArea = null;
    private QsstReport mQsstReport = null;

    private Font mFont = null;

    public LoggingPanel(QsstReport qsstReport) {
        super();
        mQsstReport = qsstReport;
        mFont = new Font(getFont().toString(), Font.PLAIN, 14);

        setLayout(new BorderLayout());
        // setBorder(BorderFactory.createTitledBorder("commond log"));

        int width = mQsstReport.getAppWidth();

        JPanel optionPanel = new JPanel(null);
        optionPanel.setPreferredSize(new Dimension(getWidth(), 25));

        mSavebtn = new JButton("Save");
        mSavebtn.setActionCommand(BUTTON_CMD_SAVE);
        mSavebtn.setMargin(new Insets(0, 0, 0, 0));
        mSavebtn.setBounds(width-130, 2, 50, 20);
        mSavebtn.setToolTipText("Save log to PC");
        mSavebtn.addActionListener(this);

        mClearbtn = new JButton("Clear");
        mClearbtn.setActionCommand(BUTTON_CMD_CLEAR);
        mClearbtn.setMargin(new Insets(0, 0, 0, 0));
        mClearbtn.setBounds(width-70, 2, 50, 20);
        mClearbtn.setToolTipText("Clear log");
        mClearbtn.addActionListener(this);

        optionPanel.add(mSavebtn);
        optionPanel.add(mClearbtn);

        mCmdDetaiArea = new JTextArea();
        mCmdDetaiArea.setEditable(false);
        mCmdDetaiArea.setFont(mFont);
        // mCmdDetaiArea.setRows(10);

        JScrollPane cmdScroll = new JScrollPane(mCmdDetaiArea);

        add(optionPanel, BorderLayout.NORTH);
        add(cmdScroll, BorderLayout.CENTER);
    }

    public void addLog(String log) {
        if (log == null) {
            return;
        }
        String head = ReportUtils.getTime();
        mCmdDetaiArea.append(head + "  " + log + "\n");
        try {
            mCmdDetaiArea.setCaretPosition(mCmdDetaiArea
                    .getLineEndOffset(mCmdDetaiArea.getLineCount() - 1));
        } catch (BadLocationException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        String commond = e.getActionCommand();
        if (commond.equals(BUTTON_CMD_SAVE)) {
            saveLog();
        } else if (commond.equals(BUTTON_CMD_CLEAR)) {
            clear();
        }

    }

    private void clear() {
        mCmdDetaiArea.setText("");
    }

    private void saveLog() {
        File saveFile;
        int ret;
        JFileChooser saveFileChooser = new JFileChooser();
        saveFileChooser.setDialogTitle("Save log");
        saveFileChooser.setAcceptAllFileFilterUsed(false);
        saveFileChooser.setSelectedFile(new File("log.txt"));

        FileNameExtensionFilter filter = new FileNameExtensionFilter(
                "qsst file(*.qsst)", FILTER_FORMATE);
        saveFileChooser.setFileFilter(filter);

        try {
            ret = saveFileChooser.showSaveDialog(this);
        } catch (HeadlessException he) {
            addLog("Save file dialog error!");
            return;
        }
        if (ret == JFileChooser.APPROVE_OPTION) {
            saveFile = saveFileChooser.getSelectedFile();
            if (!saveFile.getName().endsWith(FILTER_FORMATE)) {
                saveFile = new File(saveFile.getAbsoluteFile() + FILTER_FORMATE);
            }
            saveFile(saveFile);
        }
    }

    private boolean saveFile(File file) {
        FileOutputStream fos;
        try {
            fos = new FileOutputStream(file);
            fos.write(mCmdDetaiArea.getText().getBytes());
            fos.close();
        } catch (FileNotFoundException e) {
            addLog("File not found exception!");
            return false;
        } catch (IOException e) {
            addLog("IO exception!");
            return false;
        }
        return true;
    }
}
