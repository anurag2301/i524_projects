from __future__ import print_function, division
import cmd

class Mycmd(cmd.Cmd):
      prompt = 'mycmd >>> '
      intro = 'Mycmd.'

      def do_deploy(self, line):
              print("Deploy")

      def help_deploy(self):
              print('\n'.join([
                      'Deploy',
                      'Deploy help.'
              ]))

      def do_kill(self, line):
              print("Kill")

      def help_kill(self):
              print('\n'.join([
                      'Kill',
                      'Kill help.'
              ]))

      def do_benchmark(self, line):
              print("Benchmark")

      def help_benchmark(self):
              print('\n'.join([
                      'Benchmark',
                      'Benchmark help.'
              ]))

      def do_report(self, line):
              print("Report")

      def help_report(self):
              print('\n'.join([
                      'report',
                      'Report help.'
              ]))
              
      def do_EOF(self, line):
              print('bye, bye')
              return True


if __name__ == '__main__':
      Mycmd().cmdloop()
