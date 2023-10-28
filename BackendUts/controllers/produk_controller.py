import json
from pyramid.view import view_config, view_defaults
from pyramid.response import Response
from pyramid.request import Request

from sqlalchemy.exc import DBAPIError


from ..models import Produk


@view_defaults(route_name="produk")
class ProdukController:
    def __init__(self, request):
        self.request: Request = request

    @view_config(request_method="POST")
    def create(self):
        try:
            try:
                nama = self.request.json_body["nama"]
                harga = self.request.json_body["harga"]
                stok = self.request.json_body["stok"]
                gambar = self.request.json_body["gambar"]
            except:
                return Response(
                    content_type="application/json",
                    charset="UTF-8",
                    status=400,
                    body=json.dumps({"error": "Any Field Is Empty"}),
                )

            produk = Produk(nama=nama, harga=harga, stok=stok, gambar=gambar)
            self.request.dbsession.add(produk)
            self.request.dbsession.flush()

            return Response(
                json={
                    "message": "success create data",
                    },
                status=200,
                content_type="application/json",
            )

        except DBAPIError:
            return Response(
                json={"message": "failed create data"},
                status=500,
                content_type="application/json",
            )

    @view_config(request_method="GET")
    def read(self):
        try:
            produks = self.request.dbsession.query(Produk).all()
            return Response(
                json={
                    "data": [
                        {
                            "id": produk.id,
                            "image": produk.gambar,
                            "name": produk.nama,
                            "price": produk.harga
                        }
                        for produk in produks
                    ]
                },
                status=200,
                content_type="application/json",
            )
        except DBAPIError:
            return Response(
                json=json.dumps({"message": "failed"}),
                status=500,
                content_type="application/json",
            )

    @view_config(request_method="PUT", permission="admin")
    def update(self):
        try:
            try:
                id = self.request.json_body["id"]
                nama = self.request.json_body["nama"]
                harga = self.request.json_body["harga"]
                stok = self.request.json_body["stok"]
                gambar = self.request.json_body["gambar"]
            except:
                return Response(
                    content_type="application/json",
                    charset="UTF-8",
                    status=400,
                    body=json.dumps({"error": "id, title or content is empty"}),
                )

            produk = self.request.dbsession.query(Produk).filter_by(id=id).first()

            produk.nama = nama
            produk.harga = harga
            produk.stok = stok
            produk.gambar = gambar

            self.request.dbsession.flush()

            return Response(
                json={"message": "success"},
                status=201,
                content_type="application/json",
            )
        except DBAPIError:
            return Response(
                json={"message": "failed"},
                status=500,
                content_type="application/json",
            )

    @view_config(request_method="DELETE")
    def delete(self):
        try:
            try:
                id = self.request.json_body["id"]
            except:
                return Response(
                    content_type="application/json",
                    charset="UTF-8",
                    status=400,
                    body=json.dumps({"error": "id is empty"}),
                )

            produk = self.request.dbsession.query(Produk).filter_by(id=id).first()
            self.request.dbsession.delete(produk)
            self.request.dbsession.flush()

            return Response(
                json={"message": "success"},
                status=200,
                content_type="application/json",
            )

        except DBAPIError:
            return Response(
                json={"message": "failed"},
                status=500,
                content_type="application/json",
            )