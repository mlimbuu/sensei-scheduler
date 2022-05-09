class Scheduler(object):
    def __init__(self, scheduler, cluster): # single-host, static and dynamic
        self.scheduler = scheduler
        self.scheduler_cluster = cluster
        
    def schedule(self):
        #check for nodes with free gpus
        total_node_with_free_gpus = self.scheduler_cluster.get_total_nodes() #for test only
        for node in total_node_with_free_gpus:
            print(node)
        #attach gpus to free node 
        #release gpus from node
        #release idle nodes