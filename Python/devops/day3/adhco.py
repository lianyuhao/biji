# import shutil
# from collections import namedtuple
# import ansible.constants as C
# from ansible.executor.task_queue_manager import TaskQueueManager
# from ansible.inventory.manager import InventoryManager
# from ansible.parsing.dataloader import DataLoader
# from ansible.playbook.play import Play
# from ansible.vars.manager import VariableManager
#
# # Options是在执行ansible临时命令时，提供的选项，需要了解的选项有
# # connection是连接方式，local表示在本机执行，ssh表示ssh执行，smart表示自动选择
# # forks指的是一次同时向多少台主机发送指令
# Options = namedtuple('Options',
#                      ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
# options = Options(connection='local', module_path=['/to/mymodules'], forks=10, become=None, become_method=None,
#                   become_user=None, check=False, diff=False)
#
# # DataLoader用于解析json/ini/yaml等文件，将其转换成python的数据类型
# loader = DataLoader()  # Takes care of finding and reading yaml, json and ini files
# # 设置密码
# passwords = dict(vault_pass='secret')
#
# # 主机清单文件，表示方式有两种
# # 一种是将各个主机用冒号分隔，成为一个字符串
# # 另外一种方式是使用主机路径列表
# # inventory = InventoryManager(loader=loader, sources='localhost,')
# inventory = InventoryManager(loader=loader, sources=['myansi/hosts'])
#
# # 变量管理
# variable_manager = VariableManager(loader=loader, inventory=inventory)
#
# # 创建play源
# play_source = dict(
#     name="Ansible Play",
#     hosts='webservers',  # 在哪台主机上执行任务
#     gather_facts='no',
#     tasks=[
#
#         dict(action=dict(module='shell', args='id root'), register='shell_out'),
#         dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
#     ]
# )
#
# # 创建play对象
# play = Play().load(play_source, variable_manager=variable_manager, loader=loader)
#
# # 通过任务队列管理器执行play
# tqm = None
# try:
#     tqm = TaskQueueManager(
#         inventory=inventory,
#         variable_manager=variable_manager,
#         loader=loader,
#         options=options,
#         passwords=passwords,
#     )
#     result = tqm.run(play)  # most interesting data for a play is actually sent to the callback's methods
# finally:
#     # we always need to cleanup child procs and the structres we use to communicate with them
#     if tqm is not None:
#         tqm.cleanup()
#
#     # Remove ansible tmpdir
#     shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)

import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C


# since API is constructed for CLI it expects certain options to always be set, named tuple 'fakes' the args parsing options object
Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
options = Options(connection='ssh', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)

# initialize needed objects
loader = DataLoader() # Takes care of finding and reading yaml, json and ini files
passwords = dict(vault_pass='secret')



# create inventory, use path to host config file as source or hosts in a comma separated string
inventory = InventoryManager(loader=loader, sources='[myansible/hosts]')

# variable manager takes care of merging all the different sources to give you a unifed view of variables available in each context
variable_manager = VariableManager(loader=loader, inventory=inventory)

# create datastructure that represents our play, including tasks, this is basically what our YAML loader does internally.
play_source =  dict(
        name = "Ansible Play",
        hosts = 'web',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='id root'), register='shell_out'),
         ]
    )

# Create play object, playbook objects use .load instead of init or new methods,
# this will also automatically create the task objects from the info provided in play_source
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# Run it - instantiate task queue manager, which takes care of forking and setting up all objects to iterate over host list and tasks
tqm = None
try:
    tqm = TaskQueueManager(
              inventory=inventory,
              variable_manager=variable_manager,
              loader=loader,
              options=options,
              passwords=passwords,
          )
    result = tqm.run(play) # most interesting data for a play is actually sent to the callback's methods
finally:
    # we always need to cleanup child procs and the structres we use to communicate with them
    if tqm is not None:
        tqm.cleanup()

    # Remove ansible tmpdir
    shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)


















