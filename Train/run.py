"""
Copyright: Wenyi Tang 2017-2018
Author: Wenyi Tang
Email: wenyi.tang@intel.com
Created Date: Oct 15th 2018

Improved train/benchmark/infer script
Type --helpfull to get full doc.
"""

# Import models in development
try:
  from Exp import *
except ImportError as ex:
  pass

from importlib import import_module

import tensorflow as tf

from VSR.Tools import Run

FLAGS = tf.flags.FLAGS


def main(*args, **kwargs):
  additional_functions = {}
  callbacks = []
  callbacks += FLAGS.f or []
  callbacks += FLAGS.f2 or []
  callbacks += FLAGS.f3 or []
  if callbacks:
    m = import_module('custom_api')
    for fn_name in callbacks:
      try:
        if '#' in fn_name:
          fn_name = fn_name.split('#')[0]
        additional_functions[fn_name] = m.__dict__[fn_name]
      except KeyError:
        raise KeyError(
          "Function [{}] couldn't be found in 'custom_api.py'".format(fn_name))
  return Run.run(*args[0][1:], **additional_functions)


if __name__ == '__main__':
  tf.app.run(main)
