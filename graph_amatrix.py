"""This module implement graph using adjacent matrix"""
import collections
import copy
class Graph:
	def __init__(self, connection, n, directed=False):
		self.__n = n+1
		self.__graph = [[float('inf')]*self.__n for _ in xrange(self.__n)]
		self.__state = collections.defaultdict(dict)
		self.initilize()
		self.build_graph(connection)
	def initilize(self):
		for i in xrange(self.__n):
			self.__graph[0][0] = "*"
			if i>0:	
				self.__graph[0][i] = chr(ord('a')+i-1)
				self.__graph[i][0] = chr(ord('a')+i-1)
				self.__graph[i][i] = 0


	def build_graph(self,connections):
		for n1, n2, w in connections:
			if n2!='':
				self.__graph[n1][n2]=w

	def delete_edge(self, u,v):
		self.__graph[u][v]= float('inf')

	def print_graph(self):
		for x in self.__graph:
			print x		

	def print_state(self):
		print'{}({})'.format(self.__class__.__name__, dict(self.__state))

	def all_pair_shortest_path(self):
		def print_matrix(mat):
			for x in mat:
				print x
			print "\n"	

		def print_all_pair_sp(pi, i, j):
			if i==j:
				print i,
			elif pi[i][j]==None:
				print "print no path form {} to {}".format(i,j)
			else:
				print_all_pair_sp(pi,i,pi[i][j])
				print "-->",
				print j,

		def extend_shortest_path(L, W): # Initially L==W
			n = len(L)
			# l_dash = [[0]*n for _ in xrange(n)]
			l_dash = copy.deepcopy(W)
			for i in xrange(1,n):
				for j in xrange(1,n):
					l_dash[i][j] = float('inf')
					for k in xrange(1,n):
						l_dash[i][j] = min(l_dash[i][j], L[i][k]+W[k][j])
			return l_dash

		#  algorithm 1: slow *
		def slow_all_pair_sp(W):
			n = len(W)
			L  = copy.deepcopy(W)
			for i in xrange(2,n-1):
				L = extend_shortest_path(L,W)
			return L
		
		#*********** call algorithm 1 ***********#
		# pi = slow_all_pair_sp(self.__graph)
		# print_matrix(pi)
		#****************************************#

		# algorithm 2: fast *
		def fast_all_pair_sp(W):
			n = len(W)
			L = copy.deepcopy(W)
			m = 1
			while m < n-1:
				L = extend_shortest_path(L,L)
				m = 2*m
			return L

		#*********** call algorithm 2 ***********#
		# pi = fast_all_pair_sp(self.__graph)
		# print_matrix(pi)
		#****************************************#		

		# algorithm 3: floyd and warshal *
		def floyd_and_warshall(W):
			n = len(W)
			# ******** code to track the path ********* #
			pi = copy.deepcopy(W)
			for i in xrange(1,n):
				for j in xrange(1,n):
					if i==j or pi[i][j]==float('inf'):
						pi[i][j]= None
					else:
						pi[i][j]= i
			# ******** code to track the path ********* #
			D = copy.deepcopy(W)
			for k in xrange(1,n):
				D_0 = copy.deepcopy(D)
				pi_0 = copy.deepcopy(pi)
				for i in xrange(1,n):
					for j in xrange(1,n):
						D[i][j] = min(D_0[i][j], D_0[i][k]+D_0[k][j])
						if (D_0[i][j])<=(D_0[i][k]+D_0[k][j]):
							pi[i][j] = pi_0[i][j]
						else:
							pi[i][j] = pi_0[k][j]

			return D, pi			

		#*********** call algorithm 3 ***********#
		D,pi = floyd_and_warshall(self.__graph)
		print_matrix(D)
		print_matrix(pi)
		for i in xrange(1,len(self.__graph)):
			for j in xrange(1,len(self.__graph)):
				print "(s={}-->d={})".format(i,j),
				print_all_pair_sp(pi,i,j),
				print "\n"	

		#****************************************#	


	


if __name__=="__main__":
	conn = [
		(1,2,3), (1,3,8),(1,5,-4),
		(2,5,7), (2,4,1),
		(3,2,4),
		(4,1,2), (4,3,-5),
		(5,4,6),
		] 
	g = Graph(conn, 5, False)
	g.all_pair_shortest_path()



	
			
