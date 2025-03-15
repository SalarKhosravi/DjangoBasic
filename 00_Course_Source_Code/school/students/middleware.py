from django.http import HttpResponse
# def CustomFunctionMiddleware(get_reponse):
    # one time configuration or initialization
    # print('one time conf')

    # def middleware(request):
    #     # code executed before view is called - request
    #     print("executed CF before the view")
    #     response = HttpResponse("RESONPSE FROM FUNCTION BASED MIDDLEWARE")
    #     print('executed after the view')
    #     # code executed after view is called - response
    #     return response
    # return middleware


class CustomClassMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response


        # one time configuration or initialization
        print('one time conf')

    def __call__(self,request):
        # code executed before view is called - request
        print("executed before the view")
        # print(request.path)
        # if(request.path == '/student/get/'):
        #     print("get view is called")
        response = self.get_response(request)
        print('executed after the view')
        # code executed after view is called - response
        return response
    
    # def process_view(self,request,view_func,view_args,view_kwargs):
    #     print("called just before calling the view")
    #     # print('view name',view_func.__name__)

    #     return None

    # def process_exception(self,request,exception):
    #     print('called the process_exception')
    #     print(exception)
    #     return None
   
    def process_template_response(self,request,response):
        print('template response hook called just after the view is executed')
        response.context_data['context_from_templat_hook'] = 'something from the hook template response'
        response.context_data['name'] = 'process_template_response'
        return response