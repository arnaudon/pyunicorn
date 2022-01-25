from pyunicorn import Network, mpi


def do_one():
    net = Network.BarabasiAlbert(n_nodes=100, n_links_each=10)
    return net.global_clustering()


def master():
    n = 1000
    for _ in range(n):
        mpi.submit_call("do_one", ())
    s = sum(mpi.get_next_result() for _ in range(n))
    print(s/n)
    mpi.info()

mpi.run()
