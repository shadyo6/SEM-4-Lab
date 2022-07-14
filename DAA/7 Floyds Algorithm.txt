#include<stdio.h>

//Prototypes
int min(int,int);
void print(int [][10],int);
void floyds(int [][10],int);

void print(int D[10][10],int n)
{
	int i,j;
	for (i=1;i<=n;i++)
	{
		for (j=1;j<=n;j++)
			printf("%d ",D[i][j]);
		printf("\n");
	}
}

void floyds(int D[10][10],int n)
{
	int i,j,k;
	for (k=1;k<=n;k++) //k is the intermediate node
	{
		printf(" With %d as Intermediate Vertex ",k);
		printf(" Cost Matrix now :\n"); //Print the cost matrix
		for (i=1;i<=n;i++) //i is the intitial node
			for (j=1;j<=n;j++) //j is the destination node
				if(i==j)
					D[i][j]=0;
				else
					D[i][j]=min(D[i][j],D[i][k]+D[k][j]);  //Assigning cost among whichever is least cost
		print(D,n);
	}
}

int min(int a,int b)
{
	return (a<b)?a:b;
}

void main()
{
	int D[10][10],w,n,e,u,v,i,j;
	printf("\n Enter the number of vertices:"); //Read No of Vertices
	scanf("%d",&n);

	printf("\n Enter the Cost Matrix : \n"); //Read elements of cost matrix
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=n;j++)
			scanf("%d",&D[i][j]);
	}
	printf("\n The Initial Cost Matrix :\n");
	print(D,n);

	floyds(D,n); //Call floyd function
	printf("\n The Final Cost Matix : \n");
	print(D,n);
	printf("\n The shortest paths are:\n"); //Print the edges of all pairs
	for (i=1;i<=n;i++)
		for (j=1;j<=n;j++)
		{
			if(i!=j)
				printf("\n <%d,%d> ====> %d",i,j,D[i][j]);
		}
}

