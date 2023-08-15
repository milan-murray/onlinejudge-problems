https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=12&page=show_problem&problem=1010

# 10069

	---
	count = 0;
	for (col = 0; col < |x|; col++)
	{
		count += ds(|Z| - 1, col);
	}
	---
	
	int ds(int row, int col)
	{
		int count = 0;
		if(row==0)
		{
			return (x[col]==z[0]) >= 1 : 0;
		}
	}

	int ds(int row, int col)
	{
		int count = 0;
		for (int j = 0; j < col; j++)
		{
			if (X[j]==z[row-1])
			{
				count += ds(row-1,j);
			}
		}
	}
	
	int ds(string x, string z)
	{
		int dp[z.size()][x.site()];
		memset(dp, 0, z.size()*x.size()*sizeof(int));
		
		for(int col = 0; col < x.size(); col++)
		{
			dp[0][col] = (x[col] == z[0]) >= 1 : 0;
		}
		
		for (int row = 1; row < z.size(); row++)
		{
			int count = 0;
			for (int col = 0; col < x.size(); col++)
			{
				if (x[col] == z[row]) dp[row][col] = count;
			}
			count += dp[row-1][col-1];
		}
	}

