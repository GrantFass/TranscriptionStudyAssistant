import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UploadLecturesComponent } from './upload-lectures.component';

describe('UploadLecturesComponent', () => {
  let component: UploadLecturesComponent;
  let fixture: ComponentFixture<UploadLecturesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ UploadLecturesComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(UploadLecturesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
