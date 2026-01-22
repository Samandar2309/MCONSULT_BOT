from aiogram import Router, F
from aiogram.types import CallbackQuery

from bot.database.session import async_session_maker
from bot.db.repositories.tickets import TicketRepository
from bot.db.models import TicketStatus
from bot.keyboards.inline import close_ticket_keyboard

router = Router()


# =====================================================
# 📞 OPERATOR — TICKETNI O‘Z ZIMMASIGA OLISH
# =====================================================
@router.callback_query(F.data.startswith("take_"))
async def take_ticket_handler(callback: CallbackQuery):
    ticket_id = int(callback.data.removeprefix("take_"))
    operator = callback.from_user

    async with async_session_maker() as session:
        repo = TicketRepository(session)

        taken = await repo.take(
            ticket_id=ticket_id,
            operator_id=operator.id,
            operator_name=operator.full_name,
        )

        if not taken:
            await callback.answer(
                "❌ Bu murojaat allaqachon boshqa operator tomonidan olingan",
                show_alert=True,
            )
            return

        ticket = await repo.get(ticket_id)

    if not ticket:
        await callback.answer("❌ Ticket topilmadi", show_alert=True)
        return

    text = (
        "📩 <b>Murojaat</b>\n\n"
        f"🆔 <b>ID:</b> {ticket.id}\n"
        f"👤 <b>Ism:</b> {ticket.name}\n"
        f"📞 <b>Telefon:</b> {ticket.phone}\n"
        f"📝 <b>Xabar:</b>\n{ticket.message}\n\n"
        "Status: 🔵 <b>Jarayonda</b>\n"
        f"👨‍💻 <b>Operator:</b> {operator.full_name}"
    )

    await callback.message.edit_text(
        text=text,
        reply_markup=close_ticket_keyboard(ticket.id),
        parse_mode="HTML",
    )

    await callback.answer("✅ Murojaat sizga biriktirildi")


# =====================================================
# 🟢 / 🔴 OPERATOR — TICKETNI YOPISH
# =====================================================
@router.callback_query(F.data.startswith(("success_", "reject_")))
async def close_ticket_handler(callback: CallbackQuery):
    action, ticket_id = callback.data.split("_")
    ticket_id = int(ticket_id)

    status = (
        TicketStatus.SUCCESS
        if action == "success"
        else TicketStatus.REJECTED
    )

    operator_id = callback.from_user.id

    async with async_session_maker() as session:
        repo = TicketRepository(session)

        ticket = await repo.get(ticket_id)
        if not ticket:
            await callback.answer("❌ Ticket topilmadi", show_alert=True)
            return

        if ticket.operator_id != operator_id:
            await callback.answer(
                "❌ Bu murojaat sizga biriktirilmagan",
                show_alert=True,
            )
            return

        closed = await repo.close(
            ticket_id=ticket_id,
            status=status,
        )

        if not closed:
            await callback.answer(
                "❌ Ticketni yopib bo‘lmadi",
                show_alert=True,
            )
            return

    status_text = (
        "🟢 <b>Muvaffaqiyatli yopildi</b>"
        if status == TicketStatus.SUCCESS
        else "🔴 <b>Rad etildi</b>"
    )

    await callback.message.edit_text(
        "📩 <b>Murojaat yakunlandi</b>\n\n"
        f"🆔 <b>ID:</b> {ticket.id}\n"
        f"👤 <b>Mijoz:</b> {ticket.name}\n\n"
        f"<b>Telefon:</b> {ticket.phone}\n\n"
        f"Status: {status_text}",
        parse_mode="HTML",
    )

    await callback.answer("✅ Murojaat yopildi")
