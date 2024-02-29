# models.py

from odoo import models, fields, api

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(string='Name', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender')
    dob = fields.Date(string='Date of Birth')
    blood_group = fields.Selection([('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], string='Blood Group')
    address = fields.Text(string='Address')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    medical_records = fields.One2many('hospital.medical.record', 'patient_id', string='Medical Records')

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor'

    name = fields.Char(string='Name', required=True)
    specialization = fields.Many2one('hospital.specialization', string='Specialization')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    appointments = fields.One2many('hospital.appointment', 'doctor_id', string='Appointments')

class HospitalSpecialization(models.Model):
    _name = 'hospital.specialization'
    _description = 'Hospital Specialization'

    name = fields.Char(string='Name', required=True)

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)
    appointment_date = fields.Datetime(string='Appointment Date', required=True)
    notes = fields.Text(string='Notes')

class HospitalMedicalRecord(models.Model):
    _name = 'hospital.medical.record'
    _description = 'Hospital Medical Record'

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)
    date = fields.Datetime(string='Date', required=True, default=fields.Datetime.now)
    diagnosis = fields.Text(string='Diagnosis')
    prescription = fields.Text(string='Prescription')
    treatment = fields.Text(string='Treatment')

class HospitalBilling(models.Model):
    _name = 'hospital.billing'
    _description = 'Hospital Billing'

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
    date = fields.Datetime(string='Date', required=True, default=fields.Datetime.now)
    amount = fields.Float(string='Amount')
    notes = fields.Text(string='Notes')
