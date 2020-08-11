# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'OpenAcademy Courses'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    responsible_id = fields.Many2one(
        "res.users", string="Responsible",
        index=True, ondelete="set null")
    session_ids = fields.One2many('openacademy.session', "course_id")


class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(required=True, string="Session Name")
    start_date = fields.Date(string="Start Date")
    duration = fields.Float(digits=(6,2), string="Duaration", help="Duration in days")
    seats = fields.Integer(string="Numbers of seats")
    instructor_id = fields.Many2one(
        "res.partner", string="Instructor",
        domain=['|', ('instructor', '=', True), ('category_id.name', 'ilike', 'Teacher')])
    course_id = fields.Many2one(
        "openacademy.course", ondelete="cascade",
        string="Course", required=True)
    attendee_ids = fields.Many2many("res.partner", string="Attendees")

