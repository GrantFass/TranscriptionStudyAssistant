import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NotecardsComponent } from './notecards.component';

describe('NotecardsComponent', () => {
  let component: NotecardsComponent;
  let fixture: ComponentFixture<NotecardsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NotecardsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NotecardsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
