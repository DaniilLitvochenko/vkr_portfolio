namespace WebApplication1.Requests
{
    public class WebApplicationRequest
    {
        public double S { get; set; } = 0.0;
        public double H { get; set; } = 0.0;

        public WebApplicationRequest(HttpRequest request)
        {
            var form = request.Form.ToList();

            foreach (var param in form)
            {
                switch (param.Key.ToLower())
                {
                    case "s":
                        this.S = Convert.ToDouble(param.Value.ToArray()[0].ToString());
                        break;
                    case "h":
                        this.H = Convert.ToDouble(param.Value.ToArray()[0].ToString());
                        break;
                    default:
                        break;
                }
            }
        }
    }
}
