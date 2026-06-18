using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace QuerySense.Models
{
    public class DashboardViewModel
    {
        public decimal TotalRevenue { get; set; }

        public int TotalOrders { get; set; }

        public int TotalCustomers { get; set; }

        public decimal AverageOrderValue { get; set; }

        public string TopProduct { get; set; }

        public string TopCategory { get; set; }

        public List<RevenueTrend> RevenueTrendData {  get; set; }
    }
}