#-*- coding:utf-8 -*-

"""
This file is part of OpenSesame.

OpenSesame is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OpenSesame is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with OpenSesame.  If not, see <http://www.gnu.org/licenses/>.
"""

from libopensesame import item, generic_response
import openexp.keyboard

class keyboard_response(item.item, generic_response.generic_response):

	"""An item for collection keyboard responses"""

	description = u'Collects keyboard responses'

	def reset(self):

		"""See item."""

		self.flush = u'yes'
		self.timeout = u'infinite'
		self.auto_response = u'space'
		self.duration = u'keypress'
		self.process_feedback = True

	def prepare(self):

		"""Prepares the item."""

		item.item.prepare(self)
		generic_response.generic_response.prepare(self)
		self._flush = self.get(u'flush') == u'yes'

	def run(self):

		"""Runs the item."""

		# Record the onset of the current item
		self.set_item_onset()
		# Flush responses, to make sure that earlier responses
		# are not carried over
		if self._flush:
			self._keyboard.flush()
		self.set_sri()
		self.process_response()

	def var_info(self):

		"""
		Gives a list of dictionaries with variable descriptions.

		Returns:
		A list of (name, description) tuples.
		"""

		return item.item.var_info(self) + \
			generic_response.generic_response.var_info(self)
