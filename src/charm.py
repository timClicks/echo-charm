#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import sys
sys.path.insert(0, 'lib')

from ops.charm import CharmBase
from ops.model import ActiveStatus
from ops.main import main

class EchoConfig(CharmBase):
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.framework.observe(self.on.config_changed, self.on_config_change)

   def on_config_change(self, _event):
       message = self.model.config['message']
       self.unit.status = ActiveStatus(message)

if __name__ == "__main__":
   main(EchoConfig)
