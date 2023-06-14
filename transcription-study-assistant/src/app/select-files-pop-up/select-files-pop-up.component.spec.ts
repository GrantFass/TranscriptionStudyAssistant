import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SelectFilesPopUpComponent } from './select-files-pop-up.component';

describe('SelectFilesPopUpComponent', () => {
  let component: SelectFilesPopUpComponent;
  let fixture: ComponentFixture<SelectFilesPopUpComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SelectFilesPopUpComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SelectFilesPopUpComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
