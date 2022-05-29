using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Newtonsoft.Json;
using WebApplication1.Requests;
using WebApplication1.Services;
using WebApplication1.Structures;


namespace WebApplication1.Controllers
{
    [ApiController]
    [Route("test")]
    public class WeatherForecastController : Controller
    {
        [HttpPost]
        [HttpGet]
        [Produces("application/json")]
        [Route("index")]

        public async Task<IActionResult> Index()
        {
            return this.Json(new { result = "Hello World" });
        }

        [HttpPost]
        [HttpGet]
        [Produces("application/json")]
        [Route("get_square")]

        public async Task<IActionResult> GetSquare()
        {
            WebApplicationRequest request = new WebApplicationRequest(this.Request);

            double square = request.S * request.H;

            MyClassResponce res = new MyClassResponce();
            res.Success = "Success";
            res.Result = square;
            res.Version = "1.0";
            return this.Json(res);
        }

        [HttpPost]
        [HttpGet]
        [Produces("application/json")]
        [Route("create_calc")]

        public async Task<IActionResult> CreateCalc()
        {
            WebApplicationRequest request = new WebApplicationRequest(this.Request);

            string path = Path.Combine(Params.DataSrc, "json_settings.txt");
            List<Results> content = new List<Results>();
            string str_content = System.IO.File.ReadAllText(path); 
            if (!string.IsNullOrEmpty(str_content))
            {
                content = JsonConvert.DeserializeObject<List<Results>>(str_content);
            }
            Results elem = new Results();
            elem.uuid = Guid.NewGuid().ToString;
            elem.result = request.S * request.H;
            content.Add(elem);
            System.IO.File.WriteAllText(path, JsonConvert.SerializeObject(content));

            return this.Json(elem);
        }

    }
}
