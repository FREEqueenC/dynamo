There is an Apache-style access log located at `/app/access.log`. Please parse this access log and generate a JSON summary report saved at `/app/report.json`.

The JSON summary report must contain the following statistics:
1. `total_requests`: The total number of requests in the log file (integer).
2. `unique_ips`: The count of unique IP addresses making requests (integer).
3. `top_path`: The most frequently requested path (string).
