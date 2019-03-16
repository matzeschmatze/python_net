Python #net modules:

type #net.ping() to ping hosts
type #net.dos() to dos somme host
type #net.scan() to scan a range from hosts and check online
type #net.ssh() to perform a ssh connection

Arguments are:
   -Ping(ip, port, text_to_send, how_often, print_output 1 = True 0 = False, timeout_in_s)
   -Dos(ip, port, text_to_send, number_of_multi_treads, print_output 1 = True 0 = False)
   -Scan(von, bis, port, text_to_send, print_output 1 = True 0 = False, timeout_in_s)
   -Ssh(ip, user, passwd, command(s)_split_by_';', port)
   
Defaults are:
   -dos(ip, port = 80, text = "Attake", thrd = 10, prnt = 1)
   -scan(von, bis, port = 80, text = "Scan...", prnt = 1, timeout = 0.001)
   -ssh(ip, user, passwd, commands, port = 22)
   -ping(ip = "no", port = 80, text = "Pinging...", mal = 10, prnt = 1, timeout = 1)
   
