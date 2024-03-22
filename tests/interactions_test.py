import pytest
import time

import generator.generator
from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DragabblePage


class TestSortablePage:

    @pytest.mark.sortable
    def test_sortable(self, driver):
        sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
        sortable_page.open()
        list_before, list_after = sortable_page.change_list_order()
        assert list_before != list_after, "List items were not moved"
        grid_before, grid_after = sortable_page.change_grid_order()
        assert grid_before != grid_after, "Grid items were not moved"


class TestSelectablePage:

    @pytest.mark.selectable
    def test_selectable(self, driver):
        selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
        selectable_page.open()
        list_selectable = selectable_page.select_list_item()
        grid_selectable = selectable_page.select_grid_item()
        assert len(list_selectable) > 0, "List element was not selected"
        assert len(grid_selectable) > 0, "Grid element was not selected"


class TestResizablePage:

    @pytest.mark.resizable
    def test_resizable_box(self, driver):
        resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
        resizable_page.open()
        max_box, min_box = resizable_page.change_resizable_box()
        assert max_box == (' 500px', ' 300px'), "Max box size is not equal to 500px * 300px"
        assert min_box == (' 150px', ' 150px'), "Min box size is not equal to 150px * 150px"

    @pytest.mark.resizable
    def test_resizable(self, driver):
        resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
        resizable_page.open()
        start_area, end_area = resizable_page.change_resizable()
        assert start_area != end_area, "Resizable area was not changed"


class TestDroppablePage:

    @pytest.mark.droppable
    def test_simple_droppable(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open()
        drop_text = droppable_page.drop_simple()
        assert drop_text == 'Dropped!', "Simple Div was not dropped to Drop div"

    @pytest.mark.droppable
    def test_accept_droppable(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open()
        drop_text = droppable_page.drop_acceptable()
        assert drop_text == 'Dropped!', "Droppable Div was not accepted"

    @pytest.mark.droppable
    def test_not_accept_droppable(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open()
        drop_text = droppable_page.drop_not_acceptable()
        assert drop_text == 'Drop here', "Droppable Div was accepted"

    @pytest.mark.droppable
    def test_prevent_not_greedy(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open()
        drop_not_greedy, drop_not_greedy_inner = droppable_page.drop_prevent_not_greedy()
        assert drop_not_greedy == drop_not_greedy_inner, "Prevent Div was not dropped to not greedy div"

    @pytest.mark.droppable
    def test_prevent_greedy(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open()
        drop_greedy, drop_greedy_inner = droppable_page.drop_prevent_greedy()
        assert drop_greedy == 'Outer droppable' and drop_greedy_inner == 'Dropped!', "Prevent Div was not dropped to greedy div"

    @pytest.mark.droppable
    def test_will_revert(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open()
        position_drop, position_revert, text = droppable_page.drop_will_revert()
        assert position_drop != position_revert and text == 'Dropped!', "Revert div was not reverted"

    @pytest.mark.droppable
    def test_will_not_revert(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open()
        position_drop, position_revert, text = droppable_page.drop_will_not_revert()
        assert position_drop == position_revert and text == 'Dropped!', "Not Revert div was reverted"


class TestDragabblePage:
    @pytest.mark.dragabble
    def test_simple_draggable(self, driver):
        dragabble_page = DragabblePage(driver, 'https://demoqa.com/dragabble')
        dragabble_page.open()
        position_before, position_after = dragabble_page.simple_drag()
        assert position_before != position_after, "Simple drag was not moved"

    @pytest.mark.dragabble
    def test_axis_restricted_draggable_x(self, driver):
        dragabble_page = DragabblePage(driver, 'https://demoqa.com/dragabble')
        dragabble_page.open()
        x_before, x_after, y_before, y_after = dragabble_page.axis_restricted_x()
        assert x_before != x_after and y_before == y_after, "X only drag was not moved"

    @pytest.mark.dragabble
    def test_axis_restricted_draggable_y(self, driver):
        dragabble_page = DragabblePage(driver, 'https://demoqa.com/dragabble')
        dragabble_page.open()
        x_before, x_after, y_before, y_after = dragabble_page.axis_restricted_y()
        assert x_before == x_after and y_before != y_after, "Y only drag was not moved"

