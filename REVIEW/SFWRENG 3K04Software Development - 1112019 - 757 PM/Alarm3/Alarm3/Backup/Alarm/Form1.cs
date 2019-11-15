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
        const bool hideThem = false;                    //To hide (visible = false) components on the form
        const bool showThem = true;                     //To show (visible = true) components on the form

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
        /* Shows or hides the code buttons.
         * Shows them if h = true 
         * Hides them if h = false                  */
        /*==========================================*/
        private void CodeButtons(bool h)
        {
            lblDigit.Visible = h;
            txtInput.Visible = h;
            btnNext.Visible = h;
        }

        /*==========================================*/
        /* Shows or hides the normal (not code) 
         * buttons.
         * Shows them if h = true 
         * Hides them if h = false                  */
        /*==========================================*/
        private void NormalButtons(bool h)
        {
            btnMode.Visible = h;
            btnClear.Visible = h;
            btnOne.Visible = h;
            btnTwo.Visible = h;
            btnThree.Visible = h;
            btnFour.Visible = h;
            btnFive.Visible = h;
            btnSix.Visible = h;
            btnSeven.Visible = h;
            btnEight.Visible = h;
            btnNine.Visible = h;
            btnZero.Visible = h;
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
                NormalButtons(hideThem);
                CodeButtons(showThem);
                this.ActiveControl = txtInput;
            }
        }

        /*==========================================*/
        /* User presses NEXT - only valid (visible)
         * when specifying code digits              */
        /*==========================================*/
        private void btnNext_Click(object sender, EventArgs e)
        {
            bool codeValid, userCancels;
            MessageBoxButtons buttons = MessageBoxButtons.OKCancel;
            DialogResult result;

            userCancels = false;
            codeValid = superAlarm.setCodeString(txtInput.Text);
            if (!codeValid) 
            {
                result = MessageBox.Show("Invalid digits or string too long - try again", "Input error", buttons);
                userCancels = (result == System.Windows.Forms.DialogResult.Cancel);
            }
            if (userCancels)
            {
                NormalButtons(showThem);
                CodeButtons(hideThem);
            }
            else if (codeValid)
            {
                NormalButtons(showThem);
                CodeButtons(hideThem);
                superAlarm.setMonitoredVariable(CASAlarm.monitoredVariable.m_set);
                SetColour(Color.Yellow);
                this.ActiveControl = btnMode;
            }
            txtInput.Text = "";
            this.ActiveControl = txtInput;
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
        /* User presses 1                           */
        /*==========================================*/
        private void btnOne_Click(object sender, EventArgs e)
        {
            superAlarm.setMonitoredVariable(CASAlarm.monitoredVariable.m_one);
            if (!superAlarm.isDeviceLive())
                SetColour(oldColour);
        }

        /*==========================================*/
        /* User presses 2                           */
        /*==========================================*/
        private void btnTwo_Click(object sender, EventArgs e)
        {
            superAlarm.setMonitoredVariable(CASAlarm.monitoredVariable.m_two);
            if (!superAlarm.isDeviceLive())
                SetColour(oldColour);
        }

        /*==========================================*/
        /* User presses 3                           */
        /*==========================================*/
        private void btnThree_Click(object sender, EventArgs e)
        {
            superAlarm.setMonitoredVariable(CASAlarm.monitoredVariable.m_three);
            if (!superAlarm.isDeviceLive())
                SetColour(oldColour);
        }

        /*==========================================*/
        /* User presses 4                           */
        /*==========================================*/
        private void btnFour_Click(object sender, EventArgs e)
        {
            superAlarm.setMonitoredVariable(CASAlarm.monitoredVariable.m_four);
            if (!superAlarm.isDeviceLive())
                SetColour(oldColour);
        }

        /*==========================================*/
        /* User presses 5                           */
        /*==========================================*/
        private void btnFive_Click(object sender, EventArgs e)
        {
            superAlarm.setMonitoredVariable(CASAlarm.monitoredVariable.m_five);
            if (!superAlarm.isDeviceLive())
                SetColour(oldColour);
        }

        /*==========================================*/
        /* User presses 6                           */
        /*==========================================*/
        private void btnSix_Click(object sender, EventArgs e)
        {
            superAlarm.setMonitoredVariable(CASAlarm.monitoredVariable.m_six);
            if (!superAlarm.isDeviceLive())
                SetColour(oldColour);
        }

        /*==========================================*/
        /* User presses 7                           */
        /*==========================================*/
        private void btnSeven_Click(object sender, EventArgs e)
        {
            superAlarm.setMonitoredVariable(CASAlarm.monitoredVariable.m_seven);
            if (!superAlarm.isDeviceLive())
                SetColour(oldColour);
        }

        /*==========================================*/
        /* User presses 8                           */
        /*==========================================*/
        private void btnEight_Click(object sender, EventArgs e)
        {
            superAlarm.setMonitoredVariable(CASAlarm.monitoredVariable.m_eight);
            if (!superAlarm.isDeviceLive())
                SetColour(oldColour);
        }

        /*==========================================*/
        /* User presses 9                           */
        /*==========================================*/
        private void btnNine_Click(object sender, EventArgs e)
        {
            superAlarm.setMonitoredVariable(CASAlarm.monitoredVariable.m_nine);
            if (!superAlarm.isDeviceLive())
                SetColour(oldColour);
        }

        /*==========================================*/
        /* User presses 0                           */
        /*==========================================*/
        private void btnZero_Click(object sender, EventArgs e)
        {
            superAlarm.setMonitoredVariable(CASAlarm.monitoredVariable.m_zero);
            if (!superAlarm.isDeviceLive())
                SetColour(oldColour);
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
