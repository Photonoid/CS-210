import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

// Estimates percolation threshold for an N-by-N percolation system.
public class PercolationStats {
    double[] p;
    int T;
    Percolation percolation1;

    // Perform T independent experiments (Monte Carlo simulations) on an 
    // N-by-N grid.
    public PercolationStats(int N, int T) {
        this.T = T;
        p = new double[this.T];
        if (N <= 0 || this.T <= 0) {
            throw new IllegalArgumentException();
        }

        for (int i = 0; i < this.T; i++) {
            percolation1 = new Percolation(N);
            double count = 0.0;
            while (!percolation1.percolates()) {
                int row = StdRandom.uniform(0, N);
                int col = StdRandom.uniform(0, N);
                if (!percolation1.isOpen(row, col)) {
                    percolation1.open(row, col);
                    count++;
                }
            }
            p[i] = count / (double) (N * N); 
        }
    }    

    // Sample mean of percolation threshold.
    public double mean() {
        return StdStats.mean(p);
    }

    // Sample standard deviation of percolation threshold.
    public double stddev() {
        return StdStats.stddev(p);
    }

    // Low endpoint of the 95% confidence interval.
    public double confidenceLow() {
        return (mean() - (1.96*stddev() / Math.sqrt(T)));
    }

    // High endpoint of the 95% confidence interval.
    public double confidenceHigh() {
        return (mean() + (1.96*stddev() / Math.sqrt(T)));
    }

    // Test client. [DO NOT EDIT]
    public static void main(String[] args) {
        int N = Integer.parseInt(args[0]);
        int T = Integer.parseInt(args[1]);
        PercolationStats stats = new PercolationStats(N, T);
        StdOut.printf("mean           = %f\n", stats.mean());
        StdOut.printf("stddev         = %f\n", stats.stddev());
        StdOut.printf("confidenceLow  = %f\n", stats.confidenceLow());
        StdOut.printf("confidenceHigh = %f\n", stats.confidenceHigh());
	}
}
