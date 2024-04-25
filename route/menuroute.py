from fastapi import APIRouter, HTTPException, status, Request, Form, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError

from typing import Annotated



router = APIRouter(prefix="/orders", tags=["Orders"])
templates = Jinja2Templates(directory="templates")




@router.get('/all')
def get_all_orders(request: Request, user: UserSchema = Depends(manager.optional)):
    orders = services.get_all_orders()
    count = services.get_number_of_orders()
    return templates.TemplateResponse(
        request,
        "order/orders.html",
        context={'orders': orders, 'count': count, 'active_user': user}
    )



"add_new_order, nous recueillons les informations sur la nouvelle commande à l'aide des annotations Form()." 
"Nous créons ensuite un dictionnaire new_order avec ces informations, ainsi qu'un statut par défaut de pending."

@router.get('/add')
def ask_to_add_new_order(request: Request):
    return templates.TemplateResponse(
        "order/new_order.html",
        context={'request': request}
    )

@router.post('/add')
def add_new_order(
    client_name: Annotated[str, Form()],
    table_number: Annotated[str, Form()],
    order_details: Annotated[str, Form()],
    order_time: Annotated[str, Form()],
    client_email: Annotated[str, Form()]
):
    new_order = {
        'client_name': client_name,
        'table_number': table_number,
        'order_details': order_details,
        'order_time': order_time,
        'client_email': client_email,
        'status': 'pending'
    }
    try:
        order = OrderSchema.model_validate(new_order)
        if CheckOrder.check_order(new_order) is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid order!",
            )
    except ValidationError as er: 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid order!",
        )
    services.add_order(order)
    return RedirectResponse(url="/orders/all", status_code=302)



"Dans la fonction delete_order_by_id, nous recueillons l'ID de la commande à supprimer à l'aide de l'annotation Form(). Nous appelons ensuite la fonction delete_order_by_id du module services pour supprimer la commande de la base de données."
"Si aucune commande avec cet ID n'est trouvée, nous levons une exception HTTPException avec un code d'état HTTP_404_NOT_FOUND"
"Enfin, nous redirigeons l'utilisateur vers la page de toutes les commandes en utilisant une instance de RedirectResponse."

@router.get('/delete')
def ask_to_delete_order(request: Request):
    return templates.TemplateResponse(
        "order/delete_order.html",
        context={'request': request}
    )

@router.post('/delete')
def delete_order_by_id(order_id: Annotated[str, Form()]):
    updated_order_storage = services.delete_order_by_id(order_id)
    if updated_order_storage is not None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No order found with this ID!",
        )
    return RedirectResponse(url="/orders/all", status_code=302)






@router.get('/edit')
def ask_to_edit_order(request: Request):
    return templates.TemplateResponse(
        "order/edit_order.html",
        context={'request': request}
    )

@router.post('/edit')
def edit_order(
    order_id: Annotated[str, Form()],
    client_name: Annotated[str, Form()],
    table_number: Annotated[str, Form()],
    order_details: Annotated[str, Form()],
    order_time: Annotated[str, Form()],
    client_email: Annotated[str, Form()],
    status: Annotated[str, Form()]
):
    new_order = {
        'client_name': client_name,
        'table_number': table_number,
        'order_details': order_details,
        'order_time': order_time,
        'client_email': client_email,
        'status': status
    }
    try:
        order = OrderSchema.model_validate(new_order)
        if CheckOrder.check_order(new_order) is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid order!",
            )
    except ValidationError: 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid order!",
        )
    services.edit_order(order_id, order)
    return RedirectResponse(url="/orders/all", status_code=302)