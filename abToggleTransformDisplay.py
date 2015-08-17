#!/usr/bin/python
# encoding: utf-8

import pymel.core as pm

'''
	Автор Aleksander Bykov (mightee.cactus@gmail.com)
	
	
	Скрипт переключает отображение элементов из меню Display -> Transform display
	Порядок такой: Local rotation -> Rotate pivot -> Scale pivot -> Selection Handle -> ничего -> и все по новой.
	
	
	ИСПОЛЬЗОВАНИЕ.
	
	Чтобы применить только к последнему выбранному элементу перетащи на полку:
		
        import abToggleTransformDisplay
        abToggleTransformDisplay.ABToggleTransformDisplay( onlyOneElement = True )
		
	Чтобы применить ко всем выбранным:
	
        import abToggleTransformDisplay
        abToggleTransformDisplay.ABToggleTransformDisplay( onlyOneElement = False )
		
'''

# Создаем класс, чтобы случайно не перекрыть какую-нибудь функцию с таким же названием
class ABToggleTransformDisplay:

    # эта штука выполниться как только класс будет создан при его вызове
	def __init__(self, onlyOneElement):
			
        # просто отступ в окошке скрипта
		print "\n\n"
	        
        # к одному или нескольким элемента применяем?
		if ( onlyOneElement ) :
			self.applyToOneObject()
		else :
			self.applyToEachObject()

		
	def applyToOneObject(self):
		
		selectedList = pm.selected()
	
		if ( len(selectedList) == 0 ) :
			print "No objects selected."
			return
			
        # берем последний элемент и работаем только с ним
		selected = selectedList[len(selectedList) - 1]
		self.toggleTransformDisplay(selected)

		
	def applyToEachObject(self):
		
		selectedList = pm.selected()
	
		if ( len(selectedList) == 0 ) :
			print "No objects selected."
			return
			
        # проходим в цикле по каждому выбранному
		for selected in selectedList :
			self.toggleTransformDisplay(selected)


    # то самое место где все происходит
	def toggleTransformDisplay(self, selected) :
	
        # сначала проверям что вообще включено
		currentLocalRotation = selected.displayLocalAxis.get()
		currentRotatePivots  = selected.displayRotatePivot.get()
		currentScalePivots   = selected.displayScalePivot.get()
		currentSelectionHandles = selected.displayHandle.get()
	
        # из названия
		nothingDisplayed = not ( currentLocalRotation or currentRotatePivots or currentScalePivots or currentSelectionHandles )
		
        # если ничего, то показываем первый пункт в списке
		if ( nothingDisplayed ) :
			selected.displayLocalAxis.set(True)
			print "Local Rotation Pivot displayed."
			return
			
        # если что-то уже было включено, то нам лень разбираться, выключаем всё
		self.hideAllTransformDisplays(selected)
		
        # и переключаемся по списку из описания
		if ( currentLocalRotation ) :
			
			selected.displayRotatePivot.set(True)
			print "Rotation Pivot displayed."
			
		elif ( currentRotatePivots ) :
			
			selected.displayScalePivot.set(True)
			print "Scale Pivot displayed."
			
		elif ( currentScalePivots ) :
			
			selected.displayHandle.set(True)
			print "Selection Handle displayed."
			
		elif ( currentSelectionHandles ) :
			
			print "All transforms were hidden."
	

	# метод прячет все 4 трансформ дислея
	def hideAllTransformDisplays(self, selected) :
		selected.displayLocalAxis.set(False)
		selected.displayRotatePivot.set(False)
		selected.displayScalePivot.set(False)
		selected.displayHandle.set(False)
