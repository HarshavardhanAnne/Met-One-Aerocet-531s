#Version 0.2
#Author: Harshavardhan Anne

import serial
import sys

class Aerocet531s(object):
    _baudrate = 38400
    _port = '/dev/ttyUSB0'
    _serialObj = serial.Serial()
    _status_flag = 1    # 0 = Good, 1 = Bad
    _print_option = 0   #0 = No printing, 1 = console printing

    #constructor
    def __init__(self,baud,port,print_opt = None):
        if baud in [300,600,1200,2400,4800,9600,14400,19200,38400]:
            self._baudrate = baud
        else:
            #log error reason
            print ("(AEROCET531s): Invalid baudrate. Using default 38400")

        self._port = port

        if print_opt is None:
            self._print_option = 0
        elif print_opt == 1:
             self._print_option = print_opt
        else:
            print "(AEROCET531s): Error: print_opt invalid"
            self._print_option = 0

    def open(self):
        #log.info('Initializing AEROCET 531s unit')
        if (self._print_option): print "(AEROCET531s): Initializing device"
        self._serialObj.baudrate = self._baudrate
        self._serialObj.port = self._port
        self._serialObj.bytesize = serial.EIGHTBITS
        self._serialObj.parity = serial.PARITY_NONE
        self._serialObj.stopbits = serial.STOPBITS_ONE
        self._serialObj.timeout = 0.3
        self._serialObj.write_timeout = 0.3

        try:
            self._serialObj.open()
            if (self._print_option): print "(AEROCET531s): Serial connection established"
            self._status_flag = 0

        except serial.serialutil.SerialException:
            #send exception msg to logger stating serial connection can not be opened
            #log.ERROR('Could not open serial port %s' % self._port)
            if (self._print_option): print ("(AEROCET531s): Could not open serial port %s" % self._port)
            self._status_flag = 1

    def close(self):
        try:
            self._serialObj.close()
            if (self._print_option): print ("(AEROCET531s): Successfully closed serial port")
        except:
            if (self._print_option): print ("(AEROCET531s): Could not close port")

    def command(self, comm):
        comm = comm.upper()
        if comm == '?' or comm == 'H':
            #log.info("Command chosen is '?' or 'H'")
            return self._write_command_active(comm)
        elif comm == '1':
            #log.info("Command chosen is '1'")
            return self._write_command_active(comm)
        elif comm == '2':
            #log.info("Command chosen is '2'")
            return self._write_command_active(comm)
        elif comm == '3':
            #log.info("Command chosen is '3'")
            return self._write_command_active(comm)
        elif comm == '4':
            #log.info("Command chosen is '4'")
            return self._write_command_active(comm)
        elif comm[0:2] == 'CU':
            #log.info("Command chosen is 'CU'")
            return self._write_command_active(comm)
        elif comm[0:2] == 'ID':
            #log.info("Command chosen is 'ID'")
            return self._write_command_active(comm)
        elif comm[0:2] == 'MM':
            #log.info("Command chosen is 'MM'")
            return self._write_command_active(comm)
        elif comm == 'RV':
            #log.info("Command chosen is 'RV'")
            return self._write_command_active(comm)
        elif comm[0:2] == 'SH':
            #log.info("Command chosen is 'SH'")
            return self._write_command_active(comm)
        elif comm[0:2] == 'SK':
            #log.info("Command chosen is 'SK'")
            return self._write_command_active(comm)
        elif comm[0:2] == 'SM':
            #log.info("Command chosen is 'SM'")
            return self._write_command_active(comm)
        elif comm[0:2] == 'SR':
            #log.info("Command chosen is 'SR'")
            return self._write_command_active(comm)
        elif comm[0:2] == 'TU':
            #log.info("Command chosen is 'TU'")
            return self._write_command_active(comm)
        elif comm == "SS":
            #log.info("Command chosen is 'SS'")
            return self._write_command_active(comm)
        elif comm == 'DT':
            #log.info("Command chosen is 'DT'")
            return self._write_command_active(comm)
        elif comm[0:2] == 'OP':
            #log.info("Command chosen is 'OP'")
            return self._write_command_active(comm)
        elif comm == 'C':
            #log.info("Command chosen is 'C'")
            return self._write_command_active(comm)
        elif comm[0] == 'D':
            #log.info("Command chosen is 'D'")
            return self._write_command_active(comm)
        elif comm[0] == 'T':
            #log.info("Command chosen is 'T'")
            return self._write_command_active(comm)
        elif comm == 'E':
            #log.info("Command chosen is 'E'")
            return self._write_command_active(comm)
        elif comm == 'S':
            #log.info("Command chosen is 'S'")
            return self._write_command_active(comm)
        else:
            #log.info("Invalid command %s" % comm)
            if (self._print_option): print "(AEROCET531s): Invalid command %s" % comm
            return None

    def activate_comm_mode(self):
        if self._serialObj.is_open == True:
            if self._status_flag == 0:
                if (self._print_option): print ("Activating comm mode")
                try:
                    self._serialObj.write('\r')
                    r1 = self._serialObj.readline()
                    self._serialObj.write('\r')
                    r2 = self._serialObj.readline()
                    self._serialObj.write('\r')
                    r3 = self._serialObj.readline()
                    return None
                except:
                    if (self._print_option): print ("(AEROCET531s): Exception! Could not write or read data. Close and reopen the serial port")
                    self._status_flag = 1
                    return None

    def _write_command_active(self,comm):
        if self._serialObj.is_open == True:
            if self._status_flag == 0:
                if (self._print_option): print ("Writing command active '%s'" % (comm))
                try:
                    result_list = []
                    self._serialObj.write(comm)
                    self._serialObj.write('\r')
                    self._serialObj.readline()
                    temp = ''
                    while True:
                        temp = self._serialObj.readline()
                        if temp == '':
                            break
                        else:
                            temp = temp.rstrip('\r\n')
                            result_list.append(temp)
                    return result_list

                except Exception as e:
                    if (self._print_option): print "(AEROCET531s): Exception! Could not write or read data. Close and reopen the serial port"
                    print (e)
                    self._status_flag = 1
                    return None

    def start_sampling(self):
        if self._serialObj.is_open == True:
            if self._status_flag == 0:
                temp = self.activate_comm_mode()
                if temp is None:
                    if (self._print_option): print ("(AEROCET531s): Starting device...")
                    temp = self.command('S')
            else:
                if (self._print_option): print ("(AEROCET531s): Status flag = 1. Close and reopen serial port")
        else:
            if (self._print_option): print (")AEROCET531s): Serial port not open. Call method open()")
    def stop_sampling(self):
        if self._serialObj.is_open == True:
            if self._status_flag == 0:
                temp = self.activate_comm_mode()
                if temp is None:
                    if (self._print_option): print ("(AEROCET531s): Stopping device...")
                    temp = self.command('E')
            else:
                if (self._print_option): print ("(AEROCET531s): Status flag = 1. Close and reopen serial port")
        else:
            if (self._print_option): print ("(AEROCET531s): Serial port not open. Call method open()")

    def get_status(self):
        return self._status_flag
