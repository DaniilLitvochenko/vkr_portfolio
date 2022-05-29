using Microsoft.AspNetCore.Builder;
using WebApplication1.Services;
using System.Configuration;

namespace WebApplication1
{
    public class Startup
    {
        public Startup(IConfiguration configuration)
        {
            Params.DataSrc = configuration.GetValue<string>("Params:DataSrc");
        }
    }
}
