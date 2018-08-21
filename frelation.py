import pyecharts
from pyecharts import Graph
from collections import Iterable

class frelation():
    '''
    这个脚本用来展示机器学习中，feature的构造关系，以便于更好的观察feature的构造情况
    This script is used to display the relationships between features in machine learning.
    This script will help you find the manufacture features more easily.

    Parameters:
    ---
    title: string
        The title of whole picture
    subtitle: string
        The description of this picture

    Returns
    ---

    Examples
    ---
    fr = frelation("The Title","The subtitle")
    fr.addNodes(['a','b','c'], 0)
    fr.addNodes(['d','e'],3)
    fr.addNodes(['f','g','h'],5)
    fr.addLink('a','d','g')
    fr.addLink('d','h')
    fr.addLink('b','e','h')
    fr.addLinks([{'source':'a','target':'e'},{'source':'c','target':'e'}])
    fr.show()

    Author:
    ---
    pipdax@126.com

    Version:
    ---
    v0.0.1
    '''

    def __init__(self, title='', subtitle=''):
        self.title = title
        self.subtitle = subtitle
        self.nodes = {}  # format like {'category1':['node1','node2'], 'category2':['node3','node4']}
        self.all_nodes = [] # store all the nodes name without category, format is ['node1','node2',...]
        self.links = []  # format like [{'source':'node1','target':'node2'},{'source':'node3','target':'node4'}]
        self.categories = []  # format like [0,0,1,1,...], the same length as self.nodes values
        self.node_style = {"graph_layout": 'none', "line_color": 'red', "line_curve": 0.08,
                           "is_focusnode": True, "is_roam": True, "is_label_show": True,
                           "label_pos": 'insideLeft', "label_text_color": '#fff',
                           "label_text_size": 15, "label_emphasis_textsize": 17, }

    def addNode(self, node, category=0):
        '''
        添加一个节点，按照category分到不同的组，每一组一个颜色，相同的组在一列上
        Add one node, distributed to several groups by category, every category use one color，
        the same category show in one column.

        Parameters
        ---
        nodes:string
            One node as string
        category: int
            Choose nodes as different group, use different color.
            The max value is 20, if lager than 20, it will back from zero.

        Returns
        ---
        string list
            Current nodes that has added before
        '''
        if not isinstance(category, int) or not isinstance(node, str):
            raise TypeError("Please intput node as string and category as int")

        if category not in self.nodes.keys():
            self.nodes[category] = []

        if self.if_node_exist(node):
            print("Warning: The following nodes has the same name as add before!")
            print(node)
        else:
            self.nodes[category].append(node)
            self.all_nodes = list(set(self.all_nodes)|set([node]))
        return self.nodes

    def addNodes(self, nodes, category=0):
        '''
        同时添加多个节点，按照category分不同的组，每一组一个颜色，相同的组在一列上
        Add several nodes, split to several groups by category, every category use one color,
        the same category show in one column.

        Parameters
        ---
        nodes:string list or string
            One node as string
            Two or more nodes as string list
        category: int
            Choose nodes as different group, use different color

        Returns
        ---
        string list
            Current nodes that has added before
        '''
        if not isinstance(category, int):
            raise TypeError("Please intput category as int")

        if category not in self.nodes.keys():
            self.nodes[category] = []

        if isinstance(nodes, str):
            if self.if_node_exist(nodes):
                print("Warning: The following nodes has the same name as add before!")
                print(nodes)
            else:
                self.nodes[category].append(nodes)
                self.all_nodes = list(set(self.all_nodes)|set([nodes]))
        elif isinstance(nodes, (list, Iterable)):
            if isinstance(nodes, Iterable):
                nodes = list(nodes)
            nodes = list(set(nodes))# remove the repeat nodes
            exist_nodes = []
            for i in nodes:
                if isinstance(i, str):
                    if self.if_node_exist(i):
                        exist_nodes.append(i)
                    else:
                        self.nodes[category].append(i)
                else:
                    raise TypeError("Please intput node as string or string list")
            if exist_nodes != []:
                print("Warning: The following nodes has the same name as add before!")
                print(exist_nodes)
            self.all_nodes = list(set(self.all_nodes)|set(nodes))
        else:
            raise TypeError("Please intput node as string or string list")
        return self.nodes

    def if_node_exist(self, node):
        '''
        Check if the node has added.

        Parameters
        ---
        node: string or string list

        Returns
        ---
        True or False
            True: Exist
        '''
        if isinstance(node, str):
            if node in self.all_nodes:
                return True
            else:
                return False
        elif isinstance(node, (list, Iterable)):
            if isinstance(node, Iterable):
                node = list(node)
            exist_list = list(set(self.all_nodes)&set(node))
            if exist_list == []:
                return False
            else:
                return True


    def addLink(self, left_node, mid_node, right_node=None, cat_list=None):
        '''
        添加一个链接，可以是两个相连，也可以是三个，其中mid_node为中间节点，分别与左右两边相连
        Add one link, two or three node will be linked.
        If input two values, then this two will be linke.
        If input three values, the mid_node will be as the middle node, connect with left_node and right_node.

        Parameters
        ---
        left_node, mid_node, right_node:string
            The node that to be connected.
        cat_list: int list
            If the node is not add before, this node will add to group as the category.

        Returns
        ---
        string list
            Current links that has added before.
        '''
        if not isinstance(left_node, (str, Iterable)) or not isinstance(mid_node, (str, Iterable)):
            raise TypeError("Please intput left_node and mid node as string or string list")
        if right_node is not None and not isinstance(right_node, (str, Iterable)):
            raise TypeError("Please intput left_node and mid_node as string")

        if not isinstance(left_node, str) and isinstance(left_node, Iterable):
            for i in left_node:
                if not isinstance(i, str):
                    raise TypeError("Please intput left_node as string or string list")
        if not isinstance(mid_node, str) and isinstance(mid_node, Iterable):
            for i in mid_node:
                if not isinstance(i, str):
                    raise TypeError("Please intput mid_node as string or string list")
        if right_node is not None and not isinstance(right_node, str) and isinstance(right_node, Iterable):
            for i in right_node:
                if not isinstance(i, str):
                    raise TypeError("Please intput right_node as string or string list")

        #add node if cat_list is set
        if cat_list is not None:
            param_list = [left_node, mid_node]
            if right_node is not None:
                param_list.append(right_node)
            assert len(param_list) == len(cat_list)

            for i, cat in enumerate(cat_list):
                if not isinstance(cat, int):
                    raise TypeError("The cat_list must be int list")
                self.addNodes(param_list[i], cat_list[i])
        if isinstance(left_node, str):
            left_node = [left_node,]
        if isinstance(mid_node, str):
            mid_node = [mid_node,]
        if right_node is not None and isinstance(right_node, str):
            right_node = [right_node,]
        for left in left_node:
            for mid in mid_node:
                _link = {"source": left, "target": mid}
                self.links.append(_link)
        if right_node is not None:
            for mid in mid_node:
                for right in right_node:
                    _link = {"source": mid, "target": right}
                    self.links.append(_link)
        return self.links

    def addLinks(self, links, cat_list=None):
        '''
        添加多个链接，必须以形如[{'source':'a','target':'e'},{'source':'c','target':'e'}]的格式添加，
        每个字典为一个链接，必须包含source以及target
        Add several links, must use format as [{'source':'a','target':'e'},{'source':'c','target':'e'}].
        Every dict as one link, must include source and target.

        Parameters
        ---
        left_node, mid_node, right_node:string
            The node that to be connected.
        category: int
            Choose nodes as different group, use different color.

        Returns
        ---
        string list
            Current links that has added before.
        '''
        if not isinstance(links, (list, Iterable)):
            raise TypeError("Please uses dict list like [{'source':'node1','target':'node2'}]")
        else:
            if isinstance(links, Iterable):
                links = list(links)
        if cat_list is not None:
            assert len(links)==len(cat_list)
            for i,j in cat_list:
                if not isinstance(i, int) and not isinstance(j, int):
                    raise TypeError("cat_list must be int list")

        for i,link in enumerate(links):
            if not isinstance(link, dict) or 'source' not in link.keys() or 'target' not in link.keys():
                raise TypeError("Please uses dict list like [{'source':'node1','target':'node2'}]")
            _link = {"source": link['source'], "target": link['target']}
            if cat_list is not None:
                self.addNodes([link['source'], link['target']], cat_list[i])
            self.links.append(_link)
        return self.links

    def show(self):
        '''
        将添加的节点以及链接展示出来
        Show the nodes and links added before.

        Returns
        ---
        pyechats Graph object
            This will draw the graph oject.
        '''
        # 处理link节点，删除不在nodes中的节点
        _link_nodes = set([x['source'] for x in self.links]) | set([x['target'] for x in self.links])
        _nodes = self.all_nodes
        _del_link_nodes = _link_nodes - set(_nodes)
        self.links = list(filter(lambda x: x['source'] not in _del_link_nodes
                                           and x['target'] not in _del_link_nodes, self.links))

        graph = Graph(self.title, self.subtitle, height=len(_nodes)*25)
        nodes = []
        nodes_pos = [0, 0]
        symbol_width = max(map(len, _nodes))*10 # get the max charactor length
        symbol_width = min(max(symbol_width,80), 200) # min is 80, max is 200
        for cat_id, cats in enumerate(self.nodes.keys()):
            for node_id, cat_nodes in enumerate(self.nodes[cats]):
                self.categories.append(cats)
                nodes_pos = [cat_id * 150, node_id * 20]
                nodes.append({"name": cat_nodes,
                              "x": nodes_pos[0], "y": nodes_pos[1],
                              'symbolSize': [symbol_width, 20],
                              "symbol": 'rect',
                              "category": (cats % 20),
                              "graph_repulsion":10000})
        graph.add("", nodes, self.links, categories=self.categories, **self.node_style)

        # graph.render() I do not know why this API is not work in my environment.
        return graph

if __name__ == "__main__":
    fr = frelation("The Title", "The subtitle")
    fr.addNodes(['a', 'b', 'c'], 0)
    fr.addNodes(['d', 'e'], 3)
    fr.addNodes(['f', 'g', 'h'], 5)
    fr.addLink('a', 'd', 'g')
    fr.addLink('d', 'h')
    fr.addLink('b', 'e', 'h')
    fr.addLink(['m','a','c'],['d','e'],cat_list=[0,3])
    fr.addLinks([{'source': 'a', 'target': 'e'}, {'source': 'c', 'target': 'e'}])
    fr.show()
