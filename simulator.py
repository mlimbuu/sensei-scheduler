from cluster import Cluster
from scheduler import Scheduler

# simulator: read_trace, initialize cluster, schedule jobs
def read_trace():
    pass 
def initalize_cluster(type):
    # single node cluster
    if type=="single-host":
        cluster = Cluster(num_node_p_pool=3)
        cluster.set_cluster_spec()
    # 3-host cluster
    elif type=="3-host":
        cluster = Cluster(num_node_p_pool=3)
        cluster.set_cluster_spec()
    # multiple hosts clusters
    else:
        cluster = Cluster()
        cluster.set_cluster_spec()     
    # print cluster details    
    cluster.__str__()
    return cluster 

def schedule_jobs(cluster):
    scheduler_type = "single-host"
    # scheduler_type = "static"
    # scheduler_type = "dynamic"
    schedule_job = Scheduler(scheduler_type, cluster)
    schedule_job.schedule()

if __name__=="__main__":
    ## initialize cluster for single-host, 3-host and multiple-host clusters
    type = "single-host"
    #type = "3-host"
    cluster=initalize_cluster(type)
    schedule_jobs(cluster)