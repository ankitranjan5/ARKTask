
#include <bits/stdc++.h>
#include <iostream>

using namespace std;

const int sizen = 1000;
long long costMatrixA[sizen][sizen];
long long costMatrixB[sizen][sizen];

long long productMat[sizen][sizen];
vector<vector<long>>dp(sizen,vector<long>(sizen,-1));
vector<vector<long>>mdp(sizen,vector<long>(sizen,-1));
;

//Simple recursion  which returns the minimum cost of going from i,j to n,n
long long FindMinCostA(int i, int j, int n)
{
     if (i == n && j == n)
        return costMatrixA[i][j];
    //going out of bounds
    if (i > n || j>n)
        return 10e6;
    //going out of bounds
    if (dp[i][j]!=-1)
        return dp[i][j];
    //reaching the last cell
   
    //going down or right
    return dp[i][j] = costMatrixA[i][j] + min(FindMinCostA(i + 1, j, n), FindMinCostA(i, j + 1, n));
}
//Simple recursion which returns the maximum cost of going from i,j to n,n
long long FindMaxCostB(int i, int j, int n)
{
    //going out of bounds
    // if (i >= n)
    //     return 0;
    // //going out of bounds
    // if (j >= n)
    //     return 0;
    // //reaching the last cell
    // if (i == n - 1 && j == n - 1)
    //     return costMatrixB[i][j];
    // //going down or right
    // return costMatrixB[i][j] + max(FindMaxCostB(i + 1, j, n), FindMaxCostB(i, j + 1, n));
     if (i == n && j == n)
        return costMatrixB[i][j];
    //going out of bounds
    if (i > n || j>n)
        return -10e6;
    //going out of bounds
    if (mdp[i][j]!=-1)
        return mdp[i][j];
    //reaching the last cell
   
    //going down or right
    return mdp[i][j] = costMatrixB[i][j] + max(FindMaxCostB(i + 1, j, n), FindMaxCostB(i, j + 1, n));
}

int main()
{
    int i, j, k;
    srand(time(0));
    // initialisation
    for (i = 0; i < sizen; i++)
    {
        for (j = 0; j < sizen; j++)
        {
            costMatrixA[i][j] = 1 + rand() % 10;
            costMatrixB[i][j] = 1 + rand() % 10;
            productMat[i][j] = 0;
        }
    }

    long temp1 = FindMinCostA(0,0,sizen-1);
    long temp2 = FindMaxCostB(0,0,sizen-1);
    dp[sizen-1][sizen-1] = costMatrixA[sizen-1][sizen-1];
    mdp[sizen-1][sizen-1] = costMatrixB[sizen-1][sizen-1];

    //   for (int i = 0; i < sizen; i++)
    // {
    //     for (int j = 0; j < sizen; j++)
    //     {
    //         printf("%d  ",costMatrixA[i][j]);
    //     }
    //     printf("\n");
    // }
    //    for (int i = 0; i < sizen; i++)
    // {
    //     for (int j = 0; j < sizen; j++)
    //     {
    //         printf("%d  ",costMatrixB[i][j]);
    //     }
    //     printf("\n");
    // }

    //   for (int i = 0; i < sizen; i++)
    // {
    //     for (int j = 0; j < sizen; j++)
    //     {
    //         printf("%d  ",dp[i][j]);
    //     }
    //     printf("\n");
    // }
    //    for (int i = 0; i < sizen; i++)
    // {
    //     for (int j = 0; j < sizen; j++)
    //     {
    //         printf("%d  ",mdp[i][j]);
    //     }
    //     printf("\n");
    // }
    //creating productMat as explained in the beginning
    for (i = 0; i < sizen; i++)
    {
        for (j = 0; j < sizen; j++)
        {
            for (k = 0; k < sizen; k++)
                productMat[i][j] += dp[i][k]*mdp[k][j];
        }
    }
//      for ( i = 0; i < sizen; i++)
//    {  
//       long t = dp[i][0];
//       for ( j = 0; j < sizen; j++)
//          productMat[i][j] = t * mdp[0][j];

//       for (int k = 1; k < sizen; k++)
//       {
//          long s = 0;
//          for ( j = 0; j < sizen; j++ )
//             s += dp[i][k] * mdp[k][j];
//          productMat[i][j] = s;
//       }
//    }
    //filter of size 4 x n
    long long filterArray[4][sizen];
    for (i = 0; i < 4; i++)
    {
        for (j = 0; j < sizen; j++)
            filterArray[i][j] = rand() % 2;
    }
    // matrix of dimension (sizen/c) x 1 where c = 4
    long long finalMat[sizen / 4];
    // applying the filter
    for (i = 0; i < sizen - 4; i += 4)
    {
        long long sum = 0;
        // dot product of 4xn portion of productMat
        for (j = 0; j < sizen; j++)
        {
            for (int filterRow = 0; filterRow < 4; filterRow++)
            {
                sum += productMat[i + filterRow][j];
            }
        }
        finalMat[i / 4] = sum;
    }
    

    printf("%d \n ",FindMinCostA(0,0,sizen-1));
    printf("%d \n ",FindMaxCostB(0,0,sizen-1));
    printf("%d \n ",productMat[0][0]);

    return 0;
}