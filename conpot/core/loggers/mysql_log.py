# Copyright (C) 2013  Lukas Rist <glaslos@gmail.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.


import os
import platform
import grp


class MySQL_Logger(object):

    def __init__(self):
        # TODO: connect to database
        # TODO: invoke->create database

    def _create_db(self):
        # TODO: create database

    def log(self, event):

        #cursor.execute("INSERT INTO events(session, remote, protocol, request, response) VALUES (?, ?, ?, ?, ?)",
        #               (str(event["id"]), str(event["remote"]), event['data_type'],
        #                event["data"].get('request'), event["data"].get('response'))
        #)
        #self.conn.commit()
        #return cursor.lastrowid

    def log_session(self, session):
        pass

    def select_data(self):
        #cursor = self.conn.cursor()
        #cursor.execute("SELECT * FROM events")
        #print cursor.fetchall()
