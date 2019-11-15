using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Alarm
{
    /* Class defines the operation of the CAS Super Alarm.
     * The public interface consists of:
     *   Definition of the components of monitoredVariable
     *   Constructor
     *   setCodeString(s) uses string s to set the code, returns whether successful as a bool
     *   AlarmSounding returns true if the alarm is sounding
     *   isDeviceLive returns true if the alarm device is currently live (not off)
     *   setMonitoredVariable(m) uses monitoredVariable m as current input to the device to set the state of the device
     */
    public class CASAlarm
    {
        private const int maxCodeDigits = 3;                    //maximum number of digits in code string
        private string secretCode = "123";                      //the code string
        private enum alarmState                                 //operating states of the device
        {
            deviceOff,      //device not active
            deviceOn,       //basic state of active device
            error,          //incorrect code digit(s) entered
            good1,          //1 correct code digit entered
            good2,          //2 correct code digits entered
            alarmOn,        //trip detected - not cancelled
            alarmError,     //trip - incorrect digit(s) entered
            alarmGood1,     //trip - 1 correct digit entered
            alarmGood2      //trip - 2 correct digits entered
        }
        private alarmState opState = alarmState.deviceOff;      //current operating state - initial state is deviceOff

        private enum inputVariable                              //possible input variables
        {
            badDigit,       //incorrect code digit
            clearButton,    //clear button press
            goodDigit,      //correct code digit
            setButton,      //set button press
            trip            //trip condition
        }

        public enum monitoredVariable                           //possible monitored variables
        {
            m_one,          //1 pressed
            m_two,          //2 pressed
            m_three,        //3 pressed
            m_four,         //4 pressed
            m_five,         //5 pressed
            m_six,          //6 pressed
            m_seven,        //7 pressed
            m_eight,        //8 pressed
            m_nine,         //9 pressed
            m_zero,         //0 pressed
            m_clear,        //clear pressed
            m_set,          //set pressed
            m_trip          //trip detected
        }

        /**PUBLIC************************************************/
        /* Constructor                                          */
        /********************************************************/
        public CASAlarm()
        {
            opState = alarmState.deviceOff;
        }

        /**PUBLIC************************************************/
        /* sets secretCode to the value of the string parameter.
         * If the string parameter is not valid then function
         * returns false.  If everything ok, returns true.      */
        /********************************************************/
        public bool setCodeString(string s)
        {
            if (s.Length != maxCodeDigits) return false;
            else
            {
                for (int i = 0; i < s.Length; i++)
                    if (s[i] < '0' || s[i] > '9') return false;
            }
            secretCode = s;
            return true;
        }

        /**PUBLIC************************************************/
        /* Returns true if the alarm is (should be) sounding.
         * Returns false otherwise.                             */
        /********************************************************/
        public bool AlarmSounding()
        {
            return (opState == alarmState.alarmError || opState == alarmState.alarmGood1 ||
                    opState == alarmState.alarmGood2 || opState == alarmState.alarmOn);
        }

        /**PUBLIC************************************************/
        /* Returns true if the device is active.  Returns false
         * if the device is not active.                         */
        /********************************************************/
        public bool isDeviceLive()
        {
            return opState != alarmState.deviceOff;
        }

        /**PUBLIC************************************************/
        /* Uses the monitoredVariable m to determine the
         * appropriate inputVariable and submits that to
         * the nextState procedure to determine the next
         * operating state of the device.                       */
        /********************************************************/
        public void setMonitoredVariable(monitoredVariable m)
        {
            switch (m)
            {
                case monitoredVariable.m_one:
                    if (checkDigit('1'))
                        nextState(inputVariable.goodDigit);
                    else
                        nextState(inputVariable.badDigit);
                    break;
                case monitoredVariable.m_two:
                    if (checkDigit('2'))
                        nextState(inputVariable.goodDigit);
                    else
                        nextState(inputVariable.badDigit);
                    break;
                case monitoredVariable.m_three:
                    if (checkDigit('3'))
                        nextState(inputVariable.goodDigit);
                    else
                        nextState(inputVariable.badDigit);
                    break;
                case monitoredVariable.m_four:
                    if (checkDigit('4'))
                        nextState(inputVariable.goodDigit);
                    else
                        nextState(inputVariable.badDigit);
                    break;
                case monitoredVariable.m_five:
                    if (checkDigit('5'))
                        nextState(inputVariable.goodDigit);
                    else
                        nextState(inputVariable.badDigit);
                    break;
                case monitoredVariable.m_six:
                    if (checkDigit('6'))
                        nextState(inputVariable.goodDigit);
                    else
                        nextState(inputVariable.badDigit);
                    break;
                case monitoredVariable.m_seven:
                    if (checkDigit('7'))
                        nextState(inputVariable.goodDigit);
                    else
                        nextState(inputVariable.badDigit);
                    break;
                case monitoredVariable.m_eight:
                    if (checkDigit('8'))
                        nextState(inputVariable.goodDigit);
                    else
                        nextState(inputVariable.badDigit);
                    break;
                case monitoredVariable.m_nine:
                    if (checkDigit('9'))
                        nextState(inputVariable.goodDigit);
                    else
                        nextState(inputVariable.badDigit);
                    break;
                case monitoredVariable.m_zero:
                    if (checkDigit('0'))
                        nextState(inputVariable.goodDigit);
                    else
                        nextState(inputVariable.badDigit);
                    break;
                case monitoredVariable.m_clear:
                    nextState(inputVariable.clearButton);
                    break;
                case monitoredVariable.m_set:
                    nextState(inputVariable.setButton);
                    break;
                case monitoredVariable.m_trip:
                    nextState(inputVariable.trip);
                    break;
            }
        }

        /*------------------------------------------------------*/
        /* Uses the input variable i to determine the next      *
         * operating state of the device.                       */
        /*------------------------------------------------------*/
        private void nextState(inputVariable i)
        {
            switch (opState)
            {
                case alarmState.deviceOff:
                    if (i == inputVariable.setButton)
                        opState = alarmState.deviceOn;
                    break;
                case alarmState.deviceOn:
                    if (i == inputVariable.badDigit)
                        opState = alarmState.error;
                    else if (i == inputVariable.goodDigit)
                        opState = alarmState.good1;
                    else if (i == inputVariable.trip)
                        opState = alarmState.alarmOn;
                    break;
                case alarmState.error:
                    if (i == inputVariable.clearButton)
                        opState = alarmState.deviceOn;
                    else if (i == inputVariable.trip)
                        opState = alarmState.alarmError;
                    break;
                case alarmState.good1:
                    if (i == inputVariable.badDigit)
                        opState = alarmState.error;
                    else if (i == inputVariable.clearButton)
                        opState = alarmState.deviceOn;
                    else if (i == inputVariable.goodDigit)
                        opState = alarmState.good2;
                    else if (i == inputVariable.trip)
                        opState = alarmState.alarmOn;
                    break;
                case alarmState.good2:
                    if (i == inputVariable.badDigit)
                        opState = alarmState.error;
                    else if (i == inputVariable.clearButton)
                        opState = alarmState.deviceOn;
                    else if (i == inputVariable.goodDigit)
                        opState = alarmState.deviceOff;
                    else if (i == inputVariable.trip)
                        opState = alarmState.alarmOn;
                    break;
                case alarmState.alarmOn:
                    if (i == inputVariable.badDigit)
                        opState = alarmState.alarmError;
                    else if (i == inputVariable.goodDigit)
                        opState = alarmState.alarmGood1;
                    break;
                case alarmState.alarmError:
                    if (i == inputVariable.clearButton)
                        opState = alarmState.alarmOn;
                    break;
                case alarmState.alarmGood1:
                    if (i == inputVariable.badDigit)
                        opState = alarmState.alarmError;
                    else if (i == inputVariable.clearButton)
                        opState = alarmState.alarmOn;
                    else if (i == inputVariable.goodDigit)
                        opState = alarmState.alarmGood2;
                    break;
                case alarmState.alarmGood2:
                    if (i == inputVariable.badDigit)
                        opState = alarmState.alarmError;
                    else if (i == inputVariable.clearButton)
                        opState = alarmState.alarmOn;
                    else if (i == inputVariable.goodDigit)
                        opState = alarmState.deviceOff;
                    break;
            }
        }

        /*------------------------------------------------------*/
        /* Returns true if the character c is a correct code    *
         * digit - takes into account the current operating     *
         * state.  Returns false if the character c is not      *
         * correct.                                             */
        /*------------------------------------------------------*/
        private bool checkDigit(char c)
        {
            bool good = false;

            switch (opState)
            {
                case alarmState.deviceOff:
                case alarmState.deviceOn:
                case alarmState.alarmOn:
                    good = (c == secretCode[0]);
                    break;
                case alarmState.error:
                case alarmState.alarmError:
                    good = false;
                    break;
                case alarmState.good1:
                case alarmState.alarmGood1:
                    good = (c == secretCode[1]);
                    break;
                case alarmState.good2:
                case alarmState.alarmGood2:
                    good = (c == secretCode[2]);
                    break;
            }
            return good;
        }
    }
}
