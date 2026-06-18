using QuerySense.Models;
using System;
using System.Collections.Generic;
using System.Configuration;
using System.Data.SqlClient;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace QuerySense.Controllers
{
    public class DashboardController : Controller
    {
        // GET: Dashboard
        string cs = ConfigurationManager.ConnectionStrings["QuerySenseDB"].ConnectionString;
        public ActionResult Index()
        {
            DashboardViewModel d=new DashboardViewModel();
            SqlConnection conn=new SqlConnection(cs);

            conn.Open();

            string qry = "SELECT ISNULL(SUM(TotalAmount),0) From Orders";
            SqlCommand cmd = new SqlCommand(qry, conn);
            d.TotalRevenue=Convert.ToDecimal(cmd.ExecuteScalar());

            string qry1 = "Select count(*) from Orders";
            SqlCommand cmd1=new SqlCommand(qry1, conn);
            d.TotalOrders=Convert.ToInt32(cmd1.ExecuteScalar());

            string qry2 = "select count(*) from Customers";
            SqlCommand cmd2=new SqlCommand(qry2, conn);
            d.TotalCustomers=Convert.ToInt32(cmd2.ExecuteScalar());

            string qry3 = "select ISNULL(avg(TotalAmount),0) from Orders";
            SqlCommand cmd3=new SqlCommand(qry3, conn);
            d.AverageOrderValue=Convert.ToDecimal(cmd3.ExecuteScalar());

            string qry4 = 
            @"
            SELECT TOP 1
            p.ProductName
            FROM 
            OrderItems oi
            JOIN 
            Products p
            ON 
            oi.ProductId=p.ProductId
            GROUP BY 
            p.ProductName
            ORDER BY
            SUM(oi.Quantity) DESC
            ";
            SqlCommand cmd4=new SqlCommand(qry4, conn);
            d.TopProduct = Convert.ToString(cmd4.ExecuteScalar());

            string qry5 =
            @"
            select top 1
            c.CategoryName
            From OrderItems oi
            join
            Products p
            on
            oi.ProductId=p.ProductId
            join
            Categories c
            on 
            p.CategoryId=c.CategoryId
            Group by
            c.CategoryName
            Order by
            Sum(oi.Quantity * oi.UnitPrice) DESC
            ";
            SqlCommand cmd5=new SqlCommand(qry5, conn);
            d.TopCategory=Convert.ToString(cmd5.ExecuteScalar());

            d.RevenueTrendData = new List<RevenueTrend>();
            string qry6 =
            @"
            select
            DATENAME(MONTH, OrderDate) as MonthName,
            Sum(TotalAmount) as TotalAmount
            from Orders
            Group by
            MONTH(OrderDate),
            DATENAME(MONTH, OrderDate)
            Order by
            MONTH(OrderDate)    
            ";
            SqlCommand cmd6=new SqlCommand(qry6, conn);
            SqlDataReader dr=cmd6.ExecuteReader();

            while (dr.Read())
            {
                d.RevenueTrendData.Add(
                    new RevenueTrend
                    {
                        Month = dr["MonthName"].ToString(),
                        Revenue = Convert.ToDecimal(dr["TotalAmount"])
                    });
            }
            dr.Close();
            conn.Close();

            return View(d);
        }
    }
}