using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace Alarm
{
    public partial class Form1 : Form
    {
        int numDigits;                                  //Number of code digits entered
        string codeString;                              //secret code
        Color oldColour;                                //Original colour of Set button

        CASAlarm superAlarm;                            //Reference to CASAlarm

        /*==========================================*/
        /* Constructor
         *                                          */
        /*==========================================*/
        public Form1()
        {
            InitializeComponent();
        }

        /*==========================================*/
        /* Gets current text on Mode button         */
        /*==========================================*/
        private string getModeCaption()
        {
            return btnMode.Text;
        }

        /*==========================================*/
        /* Gets current colour of the SET button    */
        /*==========================================*/
        private Color getSetColour()
        {
            return btnMode.BackColor;
        }

        /*==========================================*/
        /* Sets colour of SET button to c           */
        /*==========================================*/
        private void SetColour(Color c)
        {
            btnMode.BackColor = c;
        }

        /*==========================================*/
        /* User presses SET                         */
        /*==========================================*/
        private void btnMode_Click(object sender, EventArgs e)
        {
            if (!superAlarm.isDeviceLive())
            {
                numDigits = 0;
                btnMode.Text = "CODE";
                codeString = "";
            }
        }

        /*==========================================*/
        /* Runs when form is loaded                 */
        /*==========================================*/
        private void Form1_Load(object sender, EventArgs e)
        {
            superAlarm = new CASAlarm();
            oldColour = getSetColour();
        }

        /*==========================================*/
        /* User presses CLEAR                       */
        /*==========================================*/
        private void btnClear_Click(object sender, EventArgs e)
        {
            superAlarm.setMonitoredVariable(CASAlarm.monitoredVariable.m_clear);
        }

        /*==========================================*/
        /* Code to process digit pressed by user    */
        /*==========================================*/
        private void handleDigit(string d, CASAlarm.monitoredVariable m)
        {
            if (getModeCaption() == "CODE")
            {
                numDigits++;
                codeString += d;
                if (numDigits >= superAlarm.getMaxCodeDigits())
                {
                    superAlarm.setCodeString(codeString);
                    numDigits = 0;
                    btnMode.Text = "SET";
                    SetColour(Color.Yellow);
                    superAlarm.setMonitoredVariable(CASAlarm.monitoredVariable.m_set);
                }
            }
            else
            {
                superAlarm.setMonitoredVariable(m);
                if (!superAlarm.isDeviceLive())
                    SetColour(oldColour);
            }
        }

        /*==========================================*/
        /* User presses 1                           */
        /*==========================================*/
        private void btnOne_Click(object sender, EventArgs e)
        {
            handleDigit("1", CASAlarm.monitoredVariable.m_one);
        }

        /*==========================================*/
        /* User presses 2                           */
        /*==========================================*/
        private void btnTwo_Click(object sender, EventArgs e)
        {
            handleDigit("2", CASAlarm.monitoredVariable.m_two);
        }

        /*==========================================*/
        /* User presses 3                           */
        /*==========================================*/
        private void btnThree_Click(object sender, EventArgs e)
        {
            handleDigit("3", CASAlarm.monitoredVariable.m_three);
        }

        /*==========================================*/
        /* User presses 4                           */
        /*==========================================*/
        private void btnFour_Click(object sender, EventArgs e)
        {
            handleDigit("4", CASAlarm.monitoredVariable.m_four);
        }

        /*==========================================*/
        /* User presses 5                           */
        /*==========================================*/
        private void btnFive_Click(object sender, EventArgs e)
        {
            handleDigit("5", CASAlarm.monitoredVariable.m_five);
        }

        /*==========================================*/
        /* User presses 6                           */
        /*==========================================*/
        private void btnSix_Click(object sender, EventArgs e)
        {
            handleDigit("6", CASAlarm.monitoredVariable.m_six);
        }

        /*==========================================*/
        /* User presses 7                           */
        /*==========================================*/
        private void btnSeven_Click(object sender, EventArgs e)
        {
            handleDigit("7", CASAlarm.monitoredVariable.m_seven);
        }

        /*==========================================*/
        /* User presses 8                           */
        /*==========================================*/
        private void btnEight_Click(object sender, EventArgs e)
        {
            handleDigit("8", CASAlarm.monitoredVariable.m_eight);
        }

        /*==========================================*/
        /* User presses 9                           */
        /*==========================================*/
        private void btnNine_Click(object sender, EventArgs e)
        {
            handleDigit("9", CASAlarm.monitoredVariable.m_nine);
        }

        /*==========================================*/
        /* User presses 0                           */
        /*==========================================*/
        private void btnZero_Click(object sender, EventArgs e)
        {
            handleDigit("0", CASAlarm.monitoredVariable.m_zero);
        }

        /*==========================================*/
        /* Trip detected                            */
        /*==========================================*/
        private void btnTrip_Click(object sender, EventArgs e)
        {
            superAlarm.setMonitoredVariable(CASAlarm.monitoredVariable.m_trip);
        }

        /*==========================================*/
        /* When timer elapses, updates alarm on
         * form                                     */
        /*==========================================*/
        private void timer1_Tick(object sender, EventArgs e)
        {
            lblAlarm.Visible = superAlarm.AlarmSounding();
        }
    }
}
