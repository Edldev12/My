import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class StudentRegistrationForm extends JFrame implements ActionListener {

// ===== Components =====
JTextField nameField, idField, emailField, phoneField, dobField;
JPasswordField passwordField;
JRadioButton male, female;
ButtonGroup genderGroup;
JComboBox<String> departmentBox;
JCheckBox javaBox, cppBox, pythonBox, jsBox, otherBox;
JTextField otherSkillField;
JList<String> courseList;
JTextArea addressArea;
JButton submitBtn, clearBtn, exitBtn;
public StudentRegistrationForm() {
setTitle("Student Registration Form");
setSize(700, 600);
setDefaultCloseOperation(EXIT_ON_CLOSE);
setLayout(new BorderLayout());
// ===== Title =====
JLabel title = new JLabel("Student Registration Form", JLabel.CENTER);
title.setFont(new Font("Arial", Font.BOLD, 20));
add(title, BorderLayout.NORTH);
// ===== MAIN PANEL =====
JPanel mainPanel = new JPanel(new GridLayout(1, 2));
// ================= LEFT SIDE =================
JPanel leftPanel = new JPanel(new GridLayout(2, 1));
// Personal Info
JPanel personal = new JPanel(new GridLayout(7, 2));
personal.setBorder(BorderFactory.createTitledBorder("Personal Information"));
nameField = new JTextField();
idField = new JTextField();
passwordField = new JPasswordField();
emailField = new JTextField();
phoneField = new JTextField();
dobField = new JTextField();
male = new JRadioButton("Male");
female = new JRadioButton("Female");
genderGroup = new ButtonGroup();
genderGroup.add(male);
genderGroup.add(female);
personal.add(new JLabel("Full Name:"));
personal.add(nameField);
personal.add(new JLabel("Student ID:"));
personal.add(idField);
personal.add(new JLabel("Password:"));
personal.add(passwordField);
personal.add(new JLabel("Gender:"));
JPanel gPanel = new JPanel();
gPanel.add(male);
gPanel.add(female);
personal.add(gPanel);
personal.add(new JLabel("DOB:"));
personal.add(dobField);
personal.add(new JLabel("Email:"));
personal.add(emailField);
personal.add(new JLabel("Phone:"));
personal.add(phoneField);
leftPanel.add(personal);
// Course Selection
String[] courses = {"Data Structures", "OOP", "Database Systems", "Operating Systems", "Web Development"};
courseList = new JList<>(courses);
JPanel coursePanel = new JPanel(new BorderLayout());
coursePanel.setBorder(BorderFactory.createTitledBorder("Course Selection"));
coursePanel.add(new JScrollPane(courseList), BorderLayout.CENTER);
leftPanel.add(coursePanel);
// ================= RIGHT SIDE =================
JPanel rightPanel = new JPanel(new GridLayout(3, 1));
// Department
JPanel deptPanel = new JPanel(new GridLayout(2, 1));
deptPanel.setBorder(BorderFactory.createTitledBorder("Department"));
String[] dept = {"Computer Science", "IT", "Software Engineering"};
departmentBox = new JComboBox<>(dept);
deptPanel.add(new JLabel("Select Department:"));
deptPanel.add(departmentBox);
// Skills
JPanel skillPanel = new JPanel(new GridLayout(6, 1));
skillPanel.setBorder(BorderFactory.createTitledBorder("Programming Skills"));
javaBox = new JCheckBox("Java");
cppBox = new JCheckBox("C++");
pythonBox = new JCheckBox("Python");
jsBox = new JCheckBox("JavaScript");
otherBox = new JCheckBox("Other");
otherSkillField = new JTextField();
skillPanel.add(javaBox);
skillPanel.add(cppBox);
skillPanel.add(pythonBox);
skillPanel.add(jsBox);
skillPanel.add(otherBox);
skillPanel.add(otherSkillField);
// Address
JPanel addressPanel = new JPanel(new BorderLayout());
addressPanel.setBorder(BorderFactory.createTitledBorder("Address"));
addressArea = new JTextArea(4, 20);
addressPanel.add(new JScrollPane(addressArea), BorderLayout.CENTER);
rightPanel.add(deptPanel);
rightPanel.add(skillPanel);
rightPanel.add(addressPanel);
mainPanel.add(leftPanel);
mainPanel.add(rightPanel);
add(mainPanel, BorderLayout.CENTER);
// ===== BUTTONS =====
JPanel btnPanel = new JPanel();
submitBtn = new JButton("Submit");
clearBtn = new JButton("Clear");
exitBtn = new JButton("Exit");
submitBtn.addActionListener(this);
clearBtn.addActionListener(this);
exitBtn.addActionListener(this);
btnPanel.add(submitBtn);
btnPanel.add(clearBtn);
btnPanel.add(exitBtn);
add(btnPanel, BorderLayout.SOUTH);
setVisible(true);
}
// ===== EVENT HANDLING =====
public void actionPerformed(ActionEvent e) {

// (a) SUBMIT
if (e.getSource() == submitBtn) {

String gender = male.isSelected() ? "Male" : female.isSelected() ? "Female" : "Not Selected";
String skills = "";
if (javaBox.isSelected()) skills += "Java ";
if (cppBox.isSelected()) skills += "C++ ";
if (pythonBox.isSelected()) skills += "Python ";
if (jsBox.isSelected()) skills += "JavaScript ";
if (otherBox.isSelected()) skills += otherSkillField.getText();
String result =
"Name: " + nameField.getText() + "\n" +
"ID: " + idField.getText() + "\n" +
"Gender: " + gender + "\n" +
"DOB: " + dobField.getText() + "\n" +
"Email: " + emailField.getText() + "\n" +
"Phone: " + phoneField.getText() + "\n" +
"Department: " + departmentBox.getSelectedItem() + "\n" +
"Skills: " + skills + "\n" +
"Courses: " + courseList.getSelectedValuesList() + "\n" +
"Address: " + addressArea.getText();
JOptionPane.showMessageDialog(this, result);
}

// (b) CLEAR
if (e.getSource() == clearBtn) {

nameField.setText("");
idField.setText("");
passwordField.setText("");
emailField.setText("");
phoneField.setText("");
dobField.setText("");
addressArea.setText("");
genderGroup.clearSelection();
javaBox.setSelected(false);
cppBox.setSelected(false);
pythonBox.setSelected(false);
jsBox.setSelected(false);
otherBox.setSelected(false);
otherSkillField.setText("");
courseList.clearSelection();
departmentBox.setSelectedIndex(0);

}
// (c) EXIT
if (e.getSource() == exitBtn) {

System.exit(0);

}

}
public static void main(String[] args) {

new StudentRegistrationForm();

}

}
