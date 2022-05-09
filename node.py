
class NodePool(object):
    def __init__(self, num_node_p_pool=20, num_gpu_p_node=8, num_cpu_p_node=92, mem_p_node=128):
        # basic node units
        self.num_gpu_p_node = num_gpu_p_node
        self.num_cpu_p_node = num_cpu_p_node
        self.mem_p_node = mem_p_node  
        # nodes
        self.pool_nodes = list() #list of node objects in a node pool
        self.num_pool_total_nodes = num_node_p_pool
        self.num_pool_free_nodes = list()
        self.num_pool_used_nodes = list() 
        # gpus
        self.pool_gpus = list() # list of gpu objects in a node pool
        self.num_pool_total_gpus = self.num_pool_total_nodes*num_gpu_p_node
        self.num_pool_used_gpus = list()
        self.num_pool_free_gpus = list()
        # cpus
        self.pool_cpus = list() # list of cpu objects in a node pool
        self.num_pool_total_cpus = self.num_pool_total_nodes*num_cpu_p_node
        self.num_pool_used_cpus = list()
        self.num_pool_free_cpus = list()
        # mem
        self.pool_mem = list() # list of mem objects in a node pool
        self.num_pool_total_mem = self.num_pool_total_nodes*mem_p_node
        self.num_pool_used_mem = list()
        self.num_pool_free_mem = list()
        
    def add_nodes(self):
        total_nodes = list()
        for i in range(self.num_pool_total_nodes):
            node = Node()
            node.add()
            total_nodes.append(node)
        self.pool_nodes = total_nodes
        return total_nodes
    
    def get_nodes(self):
        return self.pool_nodes
    
    def update_nodes(self):
        pass
    
    def get_nodes_with_free_gpus(self):
        total_free_gpu_nodes = list()
        total_nodes = self.get_nodes()
        for i in total_nodes:
            print(i)
           
    def get_nodes_with_used_gpus(self):
        total_nodes = self.get_nodes()
        for i in len(total_nodes):
            print(i)
            
    # filter nodes: hard constraints
    def filter_nodes(self):
        pass
    # score nodes: soft constraints 
    def score_nodes(self):
        pass
    
class Node(object):
    def __init__(self, num_gpu_p_node=8, num_cpu_p_node=92, mem_p_node=128):
        # cpu
        self.cpu_p_node = list() #list of cpu objects
        self.num_total_cpu_p_node = num_cpu_p_node
        self.num_used_cpu_p_node = 0
        self.num_free_cpu_p_node = 0
        # gpu
        self.gpu_p_node = list() #list of gpu objects
        self.num_total_gpu_p_node = num_gpu_p_node
        self.num_used_gpu_p_node = 0
        self.num_free_gpu_p_node = 0
        # memory
        self.memory_p_node = list() #list of memory objects
        self.num_total_mem_p_node = mem_p_node
        self.num_used_mem_p_node = 0
        self.num_free_mem_p_node = 0
        
    def add(self):
        self.num_free_gpu_p_node = self.num_total_gpu_p_node
        self.num_free_cpu_p_node = self.num_total_cpu_p_node
        self.num_free_mem_p_node = self.num_total_mem_p_node
         
    def attach_gpus(self,num_gpu_to_attach=1): #bare-mim gpu to add is 1
        self.num_free_cpu_p_node = self.num_free_cpu_p_node-num_gpu_to_attach
        
    def release_gpus(self,num_gpu_to_release=1):
        self.num_free_cpu_p_node = self.num_free_cpu_p_node+num_gpu_to_release
 
#To Do        
class GPU(object):
    pass
class CPU(object):
    pass  
class Memory(object):
    pass