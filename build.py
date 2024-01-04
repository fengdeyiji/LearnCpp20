import os
import argparse

parser = argparse.ArgumentParser(description='compile script')
parser.add_argument('--compile', default=None, choices=['config', 'debug', 'release'], type=str, help='compile')
parser.add_argument('--run', default=False, action ='store_true', help='run')
args = parser.parse_args()

def assert_do(action : str):
  print('[CMD]{}'.format(action))
  assert(0 == os.system(action))

CURRENT_DIR = os.getcwd()

if args.compile:
  need_compile = False
  compile_type = ''
  if args.compile == "config":
    compile_type = 'Debug'
  elif args.compile == "debug":
    compile_type = 'Debug'
    need_compile = True
  elif args.compile == "release":
    compile_type = 'Release'
    need_compile = True
  else:
    print("unknown options")
    exit(-1)
  COMPILE_DIR = CURRENT_DIR+"/build_{}".format(compile_type)
  if os.path.exists(COMPILE_DIR):
    assert_do("rm -rf " + COMPILE_DIR)
  assert_do("mkdir " + COMPILE_DIR)
  os.chdir(COMPILE_DIR)
  assert_do("CC=clang CXX=clang++ cmake -DCMAKE_BUILD_TYPE={} ..".format(compile_type))
  assert_do("cp compile_commands.json ..")
  if not need_compile:
    assert_do("rm -rf {}".format(COMPILE_DIR))
  else:
    assert_do("cmake --build . --config {}".format(compile_type))
if args.run:
  assert_do("./src/coroutine")