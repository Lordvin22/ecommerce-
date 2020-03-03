from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from .serializers import *
from . import serializers
from .models import *
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict
from django.http import JsonResponse, HttpResponse


class Product2ViewSets(viewsets.ModelViewSet):
    queryset = Product2.objects.all()
    serializer_class = serializers.Product2Serializer


class ProductList(generics.ListAPIView):
    queryset = Product2.objects.all()
    serializer_class = Product2Serializer


class CreateProduct(APIView):
    parser_classes = (FormParser, JSONParser, MultiPartParser)

    def post(self, request):
        serializer_class = Product2Serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_class.errors, status=status.HTTP_404_NOT_FOUND)


class ProductoDetalle(generics.ListCreateAPIView):

    def get(self, request, pk):
        todo = get_object_or_404(Product2, pk=pk)
        serializer = Product2Serializer(todo)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Product2Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = Product2.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        product = Product2.objects.get(pk=pk)
        serializer = Product2Serializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetProductId(generics.ListCreateAPIView):

    def get_queryset(self):
        queryset = Product2.objects.filter(id=self.kwargs["id"])
        get_stock = Product2.objects.get('stock')

        return queryset

    serializer_class = Product2Serializer


class GetProductName(generics.ListAPIView):
    serializer_class = Product2Serializer

    def get_queryset(self):
        """
        This view should return a list of all the PurchaseCarts for
        the user as determined by the username portion of the URL.
        """
        queryset = Product2.objects.all()
        name = self.request.query_params.get('name', None)
        queryset = queryset.filter(name=self.kwargs["name"])
        return queryset


class PurchaseCartCreate(generics.ListCreateAPIView):
    parser_classes = (FormParser, JSONParser, MultiPartParser)

    # media_type = 'text/plain'
    # serializer_class = CartSerializer
    def post(self, request):
        print request.data
        # product = Product2.objects.get(pk=pk)
        user_id = request.data.get("user_id")
        print user_id
        product_id = request.data.get("product_id")
        print product_id
        status = request.data.get("status_id")
        print status

        # queryset = Product2.objects.filter(id=self.kwargs["pk"])
        # print queryset

        # query_dict = QueryDict('', mutable=True)
        # query_dict.update(request.data)

        serializer_class = CartSerializer(data=request.data)
        print serializer_class.is_valid()
        if serializer_class.is_valid():
            serializer_class.save()
            response = {
                "message": 'success',
            }

        else:
            response = {
                "message": 'error'
            }

        return HttpResponse(response, content_type='application/json')

    def delete(self, request, pk, format=None):
        product = PurchaseCartOK.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        product = PurchaseCartOK.objects.get(pk=pk)
        serializer = PurchaseCartOK(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PurchaseCartList(generics.ListCreateAPIView):
    queryset = PurchaseCartOK.objects.all()
    serializer_class = PurchaseCartSerializer


class PurchaseCartDetail(APIView):

    def get(self, request, pk1):
        PurchaseCart1 = PurchaseCartOK.objects.get(pk=pk1)
        serializer = PurchaseCartSerializer(PurchaseCartOK)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        product = PurchaseCartOK.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        product = PurchaseCartOK.objects.get(pk=pk)
        serializer = PurchaseCartSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserType(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("pass")
        actual_user = User.objects.get(username=username)

        if password == actual_user.password:
            print [request.data]
            response = {
                "message": 'success',
                "id": actual_user.id,
                "type": str(actual_user.type),
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            print ('no entro')
            response = {
                "message": 'error'
            }

            return Response(response, status=status.HTTP_403_FORBIDDEN)


class UserCreate(generics.ListCreateAPIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def post(self, request):
        print [request.data]
        serializer_class = UserSerializer(data=request.data)
        print serializers
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


class CartCreate(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Product2.objects.filter(id=self.kwargs["id"])
        return queryset

    serializer_class = Product2Serializer

    def put(self, request, pk):
        queryset = Product2.objects.filter(pk=pk)
        print queryset


class Javi(APIView):
    parser_classes = (FormParser, JSONParser, MultiPartParser)

    def post(self, request):
        print [request.data]
        serializer_class = UserSerializer(data=request.data)
        # permission_classes = [rest_permissions.IsAuthenticated]
        print serializer_class
        if serializer_class.is_valid():
            serializer_class.save()
        else:
            return Response({'status': "error"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'received data': request.data}, status=status.HTTP_201_CREATED)

        # print [request.data]


class GetUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class PurchaseCartViewUser(generics.ListCreateAPIView):

    def get_queryset(self):
        response_list = []
        queryset = PurchaseCartOK.objects.filter(id=self.kwargs["pk"])
        return queryset

    serializer_class = PurchaseCartSerializer


# product_name, quantity, price, id

@csrf_exempt
def getPurchaseCartHistory(request):
    print " Is in"
    response_list = []
    product_id = request.POST.get('cart_id')
    PurchaseCarts = PurchaseCartOK.objects.filter(cart_id=product_id)

    for p in PurchaseCarts:
        print p.pk
        data = {
            "product_name": p.product.name,
            "price": p.product.price,
            "product_id": p.product.pk
        }
        response_list.append(data)

    return HttpResponse(response_list, content_type='application/json')


@csrf_exempt
def computeTicketValue(request):
    if request.method == 'POST':
        cart_id = request.POST.get('cart_id')  # el string es como lo manda en el request
        print cart_id
        total = 0

        cart = Product2.objects.filter(id=cart_id)

        for c in cart:
            total = c.price

        return HttpResponse({"total_amount": str(total)}, content_type='application/json')


@csrf_exempt
def BuyProduct(request):
    response_list = []
    if request.method == 'POST':
        total = 0
        a = 0
        cart_id = request.POST.get('cart_id')
        product_id = request.POST.get('pk')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        print "qu" + quantity
        print product_id
        print price
        product = Product2.objects.get(pk=product_id)
        cart_id = Cart.objects.get(pk=cart_id)
        print cart_id
        purchase = PurchaseCartOK.save()
        product.stock -= int(quantity)
        total = int(quantity) * product.price
        print "total" + str(total)
        a = 5 * 3
        print a
        if product.stock > 0:
            purchase.save()

            data = {
                "status": 1,
                "name": product.name,
                "price": total,
                "stock": product.stock
            }
            response_list.append(data)

        else:
            return HttpResponse('error')

        print product.stock

        # for p in Product2:
        # PurchaseCartOK.save()
        return HttpResponse(response_list, content_type='application/json')

    # return Response(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@csrf_exempt
def createCart(request):
        response_list = []
        if request.method == 'POST':
            user_id = request.POST.get("user_id")
            cart = Cart()

            for c in cart:
                data = {
                    "id": c.id,
                    "user_id": c.user_id,
                    "name": c.user.username

                }
                c.save()
            response_list.append(data)

            print user_id

        return HttpResponse(response_list, content_type='application/json')







@csrf_exempt
def createCart(request):
    response_list = []
    if request.method == 'POST':
        user_id = request.POST.get("user_id")
        cart = Cart.objects.filter(id=user_id)

        for c in cart:
            data = {
            "id": c.id,
            "user_id":c.user_id,

        }
        response_list.append(data)

        print user_id
        #cart.save()
    return HttpResponse(response_list, content_type='application/json')












@csrf_exempt
def createCart(request):
    response_list = []
    form = Cart()
    if request.method == 'POST':
        user_id = request.POST.get("user_id")
        cart = Cart.objects.filter(user_id=user_id)
        form = Cart(request.POST)
        for c in cart:
            data = {
            "id": c.id,
            "user_id":c.user_id,
            "name": c.user.username

        }
        response_list.append(data)

        print user_id
        c.save()
    return HttpResponse(response_list, content_type='application/json')



  form = Cart(request.POST)
        for c in cart:
            data = {
            "id": c.id,
            "user_id":c.user_id,
            "name": c.user.username

        }
        c.save()
        response_list.append(data)

try:
    product_id = request.POST.get('cart_id')
    PurchaseCarts = PurchaseCartOK.objects.filter(cart_id=product_id)
except PurchaseCartOK.DoesNotExist: