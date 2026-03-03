# def check_scope():
#     def local():
#         test = "local"

#     def non_local():
#         nonlocal test
#         test = "non_local"

#     def do_global():
#         global test
#         test = "global"

#     test = "default"


# check_scope()
# local()
# print(test)
# non_local()
# print(test)
# do_global()
# print(test)


# test = "wow"
# check_scope()
# print(test)

#
# def do_global():

#     def do_non_local():
#         nonlocal test
#         test = "non_local"

#         global do_local

#         def do_local():
#             global test
#             test = "local"

#     test = "default"
#     do_non_local()
#     do_local()

#     print(test)


# test = "wow"
# do_global()
# do_local()
# print(test)
