from node import NodePool, Node
class Cluster(object):
    def __init__(self,num_pools=1,num_node_p_pool=20, num_gpu_p_node=8, num_cpu_p_node=92, mem_p_node=128):
        # basic node units for cluster
        self.num_gpu_p_node = num_gpu_p_node
        self.num_cpu_p_node = num_cpu_p_node
        self.mem_p_node = mem_p_node 
        self.num_node_pools = num_pools
        self.num_node_p_pool = num_node_p_pool
        
        # default cluster resource values
        self.cluster_total_node_pools = self.num_node_pools
        self.cluster_total_nodes = self.num_node_pools*num_node_p_pool
        self.cluster_total_gpus = self.cluster_total_nodes*num_gpu_p_node
        self.cluster_total_cpus = self.cluster_total_nodes* num_cpu_p_node
        self.cluster_total_memory = self.cluster_total_nodes*mem_p_node
        ## cluster resource values initialized
        self.cluster_total_used_nodes = 0
        self.cluster_total_free_nodes = 0
        
        self.cluster_total_used_gpus = 0 # our decision factor , objects
        self.cluster_total_free_gpus = 0
        ## cluster resource values as objects
        self.cluster_node_pools = list()
        self.cluster_nodes = list()
        
    def get_total_node_pools(self):
        return self.cluster_node_pools
    
    def get_total_nodes(self):
        return self.cluster_nodes
              
    def __str__(self):
        print('\n+++++++++++Cluster Information+++++++++++++++')
        print('Total Node Pools:%d, Total Avail Nodes:%d, Total Avail GPUS:%d' % (self.cluster_total_node_pools, self.cluster_total_nodes, self.cluster_total_gpus))
        print('Total Free Nodes:%d, Total Free GPUs:%d' % (self.cluster_total_free_nodes, self.cluster_total_free_gpus))
        print('\n')
    # bare-minimum cluster initialization    
    def set_cluster_spec(self):
        # add nodes to node pools
        list_of_nodes_per_pool = list()
        list_of_cluster_nodes = list()
        list_of_node_pools = list()
        for i in range(self.cluster_total_node_pools):
            node_pool = NodePool(num_node_p_pool=self.num_node_p_pool)
            list_of_nodes_per_pool=node_pool.add_nodes()
            list_of_cluster_nodes =[i for i in list_of_nodes_per_pool] 
            node_pool.num_pool_free_nodes = self.num_node_p_pool
            node_pool.num_pool_free_gpus = self.num_node_p_pool*self.num_gpu_p_node
            list_of_node_pools.append(node_pool)
            
        # added resources in cluster  
        self.cluster_node_pools = list_of_node_pools
        self.cluster_nodes = list_of_cluster_nodes
        # added free resources in cluster
        self.cluster_total_free_nodes = self.cluster_total_nodes
        self.cluster_total_free_gpus = self.cluster_total_gpus
                
       
           

    

            